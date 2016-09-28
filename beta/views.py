from django.shortcuts import render, get_object_or_404, redirect
from beta.models import *
from beta.choices import * #ONLINE_SHOPPING, ENTERPRISE, ENTERTAINMENT, FINSEC, ON_DEMAND, SOCIAL_SERVICES
from beta.models import Startup
from django.core.exceptions import ObjectDoesNotExist
from beta.forms import *
from beta.scripts import *
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from djqscsv import render_to_csv_response

def index(request):
    """This function renders all the beta startups"""
    #Filters all published = True and excluded status = live
    beta_published = Startup.objects.filter(pub_status='Published').order_by("-pub_date")
    #beta_published = beta.exclude(promoted=True)
    #user_signup = SignUp.objects.all()
    paginator = Paginator(beta_published, 40) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        published = paginator.page(page)
    except PageNotAnInteger:
        published = paginator.page(1)
    except EmptyPage:
        published = paginator.page(paginator.num_pages)
    
    #Filters all promoted. This would be used to match a given duration
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    new_startups = "Beta Startups"
    context = {'beta_published':published, 'beta_promoted':promoted,
            'beta':new_startups}
    return render(request, 'beta/index.html', context)

def archives(request):
    """This view function filters a the startups with status as live"""
    archived = Startup.objects.filter(published=True)
    archived_startups = archived.filter(status="Live")
    paginator = Paginator(archived_startups, 4) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        published = paginator.page(page)
    except PageNotAnInteger:
        published = paginator.page(1)
    except EmptyPage:
        published = paginator.page(paginator.num_pages)
    #Filters all promoted. This would be used to match a given duration
    promoted = Startup.objects.filter(promoted=True).order_by("?")[:4]
    old_startups = "Archived"
    context = {'archived_startups': published,
               'beta_promoted':promoted, 'beta':old_startups}
    return render(request, 'beta/index.html', context)

def newest(request):
    """These are the list of all the startups that have their newest=True on the startup model"""
    newest_startups = Startup.objects.filter(newest=True)
    paginator = Paginator(newest_startups, 4) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        newest_strt = paginator.page(page)
    except PageNotAnInteger:
        newest_strt = paginator.page(1)
    except EmptyPage:
        newest_strt = paginator.page(paginator.num_pages)
    #Filters all promoted. This would be used to match a given duration
    promoted = Startup.objects.filter(promoted=True).order_by("?")[:4]
    new_startups = "Newest"
    context = {'newest_startups': newest_strt,
               'beta_promoted':promoted, 'beta':new_startups}
    return render(request, 'beta/index.html', context)


    
def beta_details(request, ID, startup_id):
    """This view function renders the beta details"""
    try:
        beta_details = get_object_or_404(Startup, id=ID, startup=startup_id)
    except ObjectDoesNotExist:
        beta_details = None
    #team = Team.objects.filter(startup_id=beta_details.startup_id)
    teams = beta_details.team_set.all()
    num_startups = beta_details.signup_set.all()
    len_startups = num_startups.count()
    print 'The number of signups', num_startups.count()
    related = Startup.objects.filter(tag=beta_details.tag)
    related_startups = related.exclude(startup_id=beta_details.startup_id).order_by("?")[:4]
    
    context = {'beta_details': beta_details, 'teams':teams,
               'related_beta':related_startups,'signups':len_startups}
    return render(request, 'beta/beta_details.html', context)

@login_required
def beta_user(request):
    """This function renders all the startups submitted by the user for beta"""
    #user_beta = Startup.objects.filter(user=request.user)
    me = get_object_or_404(User, email=request.user.email)
    all_my_signups = me.signup_set.all()
    context = {'my_signups':all_my_signups}
    return render(request, 'beta/user_beta.html', context)

@login_required
def mystartup(request):
    """This function filters all the startups submitted by the user"""
    user_beta = Startup.objects.filter(user=request.user)
    context = {'user_beta':user_beta}
    return render(request, 'beta/mystartup.html', context)

@login_required
def beta_user_details(request, ID, startup_id):
    """This view function renders the beta startup details of the login user"""
    #beta_user = get_object_or_404(Startup, startup_id=startup_id)
    beta_user = get_object_or_404(Startup, id=ID, startup=startup_id)
    teams = beta_user.team_set.all()
    print "This is a ", beta_user.pub_status == "Published"
    signups = beta_user.signup_set.all()
    len_signups = signups.count()
    if request.method == "GET":
        # try:
        #     beta_user = get_object_or_404(Startup, startup_id=startup_id)
        #     submit_beta_form = StartupForm(instance=beta_user, prefix="submit_beta")
        # except ObjectDoesNotExist:
        #     beta_user = StartupForm(request.FILES, prefix="submit_beta")
        # except ObjectDoesNotExist:
        #     beta_user = None
        add_team_form = TeamForm()
    if request.method == "POST":
        # try:
        #     beta_user = get_object_or_404(Startup, startup_id=startup_id)
        #     submit_beta_form = StartupForm(request.POST, instance=beta_user, prefix="submit_beta")
        # except ObjectDoesNotExis:
        #     submit_beta_form = StartupForm(request.POST, request.FILES, prefix="submit_beta")
        add_team_form = TeamForm(request.POST, request.FILES)
        if add_team_form.is_valid():
            team = add_team_form.save(commit=False)
            team.startup = beta_user
            team.save()
            return redirect('beta:index')
        else:
            print add_team_form.errors
    
    context = {"beta_details":beta_user, 'teams': teams, 'add_team':add_team_form,
               'len_signups':len_signups}
    return render(request, 'beta/beta_user_details.html', context)

def join_testers(request):
    """This function submits people willing to join testers community"""
    if request.method == "POST":
        tester_form = TesterForm(request.POST)
        if tester_form.is_valid():
            testers = tester_form.save(commit=False)
            testers.user = request.user
            testers.save()
            return redirect("beta:index")
        else:
            print tester_form.errors
    else:
        tester_form = TesterForm()
    context = {'tester_form': tester_form}
    return render(request, 'beta/beta_form.html', context)

@login_required
def submit_beta(request):
    """This function submits beta startup"""
    if request.method == "POST":
        try:
            logo = Default.objects.get(pk=1)
        except ObjectDoesNotExist:
            logo = None
        submit_beta_form = StartupForm(request.POST, request.FILES)
        if submit_beta_form.is_valid():
            beta_form = submit_beta_form.save(commit=False)
            beta_form.user = request.user
            beta_form.startup_id = beta_id()
            beta_form.pub_status = 'Pending'
            #beta_form.status = request.POST.get('status')
            #print "I need to print", beta_form.status
            print 'startup_id:', beta_form.startup_id
            beta_form.status = 'Beta'
            #Populating tag field based on the category
            for tags in ONLINE_SHOPPING:
                if beta_form.category in tags:
                    beta_form.tag = "Online Shopping"
            for tags in ENTERTAINMENT:
                if beta_form.category in tags:
                    beta_form.tag = "Entertainment"
            for tags in FINSEC:
                if beta_form.category in tags:
                    beta_form.tag = "FINSEC"
            for tags in ENTERPRISE:
                if beta_form.category in tags:
                    beta_form.tag = "Enterprise"
            for tags in ON_DEMAND:
                if beta_form.category in tags:
                    beta_form.tag = "On Demand Services"
            for tags in SOCIAL_SERVICES:
                if beta_form.category in tags:
                    beta_form.tag = "Social Services"
            #Populating the regions
            for region in EAST_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "East Africa"
            for region in WEST_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "West Africa"
            for region in CENTRAL_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "Central Africa"
            for region in SOUTHERN_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "South Africa"
            for region in NORTHERN_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "North Africa"
            plaintext = get_template('email_notifications/submit_beta.txt')
            html_text     = get_template('email_notifications/submit_beta.html')
            d = Context({'startup': request.POST.get('startup'),
                         'logo': logo,
                         'first_name': request.user.first_name,
                         #'last_name': request.POST.get('last_name'),
                         })
            subject = "Your Startup" + " " + request.POST.get('startup') + " " + "has been received"
            email = "uzoheaven@gmail.com"
            recipients = [request.user.email,]
            print 'recipients', recipients
            text_content = plaintext.render(d)
            html_content = html_text.render(d)
            msg = EmailMultiAlternatives(subject, text_content, email, recipients)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            beta_form.save()
            #obj = Startup.objects.get(startup_id=beta_form.startup_id)
            return redirect('beta:index')
            #return redirect('beta_user_details', ID=ID, startup_id=beta_form.startup_id)
        else:
            print submit_beta_form.errors
    else:
        submit_beta_form = StartupForm()
    context = {'beta_form': submit_beta_form}
    return render(request, 'beta/submit_beta.html', context)

@login_required
def edit_beta(request, startup_id):
    """This function submits beta startup"""
    if request.method == "POST":
        try:
            beta_user = get_object_or_404(Startup, startup_id=startup_id)
            submit_beta_form = StartupForm(request.POST, instance=beta_user)
        except ObjectDoesNotExis:
            submit_beta_form = StartupForm(request.POST, request.FILES)
    
        if submit_beta_form.is_valid():
            beta_form = submit_beta_form.save(commit=False)
            beta_form.user = request.user
            beta_form.pub_status = "Pending"
            beta_form.save()
            return redirect('beta:index')
        else:
            print submit_beta_form.errors
    else:
        try:
            beta_user = get_object_or_404(Startup, startup_id=startup_id)
            submit_beta_form = StartupForm(instance=beta_user)
        except ObjectDoesNotExist:
            submit_beta_form = StartupForm(request.FILES)
        except ObjectDoesNotExist:
             submit_beta_form = None
    context = {'edit_beta': submit_beta_form, 'beta_user':beta_user}
    return render(request, 'beta/edit_startup.html', context)

@login_required
def delete_startup(request, startup_id):
    """This view function deletes a startup"""
    del_startups = Startup.objects.get(startup_id=startup_id)
    del_startups.delete()
    return redirect('beta:index') 


def test_beta(request):
    """This function submits beta startup"""
    if request.method == "POST":
        test_beta_form = BetaTestForm(request.POST, request.FILES)
        if test_beta_form.is_valid():
            test_form = test_beta_form.save(commit=False)
            test_form.user = request.user
            test_form.test_id = beta_id()
            test_form.status = "Pending"
            test_form.save()
            return redirect("beta:index")
        else:
            print test_beta_form.errors
    else:
        test_beta_form = BetaTestForm()
    context = {'test_form': test_beta_form}
    return render(request, 'beta/beta_form.html', context)
    
def testing_app(request):
    """This view function renders all the test startups app"""
    test_application = BetaTest.objects.filter(user=request.user)
    #if request.method == "GET":
    add_team_form = TeamForm()
    context = {'test_app':test_application}
    return render(request, 'beta/testing_app.html', context)
 
@login_required   
def delete_team(request, startup_id):
    """This view function deletes team"""
    del_team = Team.objects.get(id=startup_id)
    del_team.delete()
    return redirect('beta:index')            

def edit_testing(request, startup_id):
    if request.method == "POST":
        try:
            beta_user = get_object_or_404(BetaTest, test_id=startup_id)
            testing_form = BetaTestForm(request.POST, instance=beta_user)
        except ObjectDoesNotExist:
            testing_form = BetaTest(request.POST, request.FILES)
        if testing_form.is_valid():
            testing = testing_form.save(commit=False)
            testing.user = request.user
            #testing.test_id = test_id
            testing.save()
            return redirect('beta:index')
        else:
            print testing_form.errors
    else:
        try:
            beta_user = get_object_or_404(BetaTest, test_id=startup_id)
            testing_form = BetaTestForm(instance=beta_user)
        except ObjectDoesNotExist:
            testing_form = BetaTestForm(request.FILES)
        except ObjectDoesNotExist:
            testing_form = None
    context = {'edit_testing':testing_form, 'beta_user':beta_user}
    return render(request, 'beta/edit_testing.html', context)


@login_required
def signup(request, ID, startup_id):
    startups = get_object_or_404(Startup, id=ID, startup=startup_id)
    create_signup = SignUp.objects.get_or_create(user=request.user, startup=startups)
    if create_signup[1] == False:
        print 'create_signup1', create_signup[0].startup.startup
        signedup_startup = create_signup[0].startup.startup
        context = {'signedup': create_signup, 'signedup_startup': signedup_startup}
        return render(request, 'beta/signup_confirmation.html', context)
    else:
        print 'create_signup2', create_signup[0].startup.startup
        not_signedup_startup = create_signup[0].startup.startup
        context = {'not_signedup':create_signup, 'not_signedup_startup': not_signedup_startup}
        # plaintext = get_template('email_notifications/signup.txt')
        # html_text     = get_template('email_notifications/signup.html')
        # d = Context({'startup': startups.startup,
        #              'logo': startups.logo,
        #              'first_name': request.user.first_name,
        #              'last_name': request.user.last_name,})
        # subject = "Thanks for subscribing to " + startups.startup
        # email = "uzoigweiroh@gmail.com"
        # recipients = [request.user.email,]
        # text_content = plaintext.render(d)
        # html_content = html_text.render(d)
        # msg = EmailMultiAlternatives(subject, text_content, email, recipients)
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
        # create_signup.save()
        return render(request, 'beta/signup_confirmation.html', context)

@login_required
def admin_signups(request, startup_id):
    startup = get_object_or_404(Startup, startup_id=startup_id)
    user_signups = startup.signup_set.all()
    #Pagination for all the signups in the admin for a user page/startup 
    paginator = Paginator(user_signups, 40) #Show 40 startups per page
    page = request.GET.get('page')
    try:
        signups = paginator.page(page)
    except PageNotAnInteger:
        signups = paginator.page(1)
    except EmptyPage:
        signups = paginator.page(paginator.num_pages)
    admin_signups = user_signups
    len_signups = user_signups.count()
    print 'print this for me', startup.startup
    context = {'user_signups': signups,
               'len_signups':len_signups, 'startup': startup}
    return render(request, 'beta/admin_signups.html', context)

@login_required
def signups(request, startup_id):
    startup = get_object_or_404(Startup, startup_id=startup_id)
    user_signups = startup.signup_set.all()
    #Pagination for all the signups in the user admin page/startup 
    paginator = Paginator(user_signups, 40) #Show 40 startups per page
    page = request.GET.get('page')
    try:
        signups = paginator.page(page)
    except PageNotAnInteger:
        signups = paginator.page(1)
    except EmptyPage:
        signups = paginator.page(paginator.num_pages)
    admin_signups = user_signups
    len_signups = user_signups.count()
    print 'print this for me', startup.startup
    context = {'user_signups': signups,
               'len_signups':len_signups, 'startup': startup}
    return render(request, 'beta/signup.html', context)

def export_signups(request, startup_id):
    startup = get_object_or_404(Startup, startup_id=startup_id)
    print "I need this printed first", startup
    user_signups = startup.signup_set.all().values('user__first_name', 'user__last_name', 'user__email')
    print "I need this printed", user_signups
    return render_to_csv_response(user_signups)

def test_invites(request):
    try:
        beta_test = get_object_or_404(Tester, user=request.user)
    except ObjectDoesNotExist:
        beta_test = None
    invites = BetaTest.objects.filter(region=beta_test.region)
    for invite in invites:
        print 'I need this:', invite
    context = {'invites':invites}
    return render(request, 'beta/invitations.html', context)

def activities(request):
    pass
    # me = get_object_or_404(User, email=request.user.email)
    # all_my_signups = me.signup_set.all()
    # comments = Comment.objects.filter(user=request.user)
    # print 'This is my comment', comments
    # context = {'my_signups':all_my_signups, 'comments': comments}
    # return render(request, 'beta/activities.html', context)

def regions(request, startup_id):
    regions_startups = Startup.objects.filter(pub_status='Published', region=startup_id).order_by('-pub_date')
    a_region = regions_startups[:1]
    len_region = regions_startups.count()
    paginator = Paginator(regions_startups, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        region_strt = paginator.page(page)
    except PageNotAnInteger:
        region_strt = paginator.page(1)
    except EmptyPage:
        region_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'regions':regions_startups, 'a_region': a_region,
               'len_region':len_region, 'beta_promoted':promoted, 'region_strt':region_strt}
    return render(request, 'beta/regions.html', context)

def country(request, startup_id):
    country_startups = Startup.objects.filter(pub_status='Published', country=
                    startup_id).order_by('-pub_date')
    a_country = country_startups[:1]
    len_country = country_startups.count()
    print "country_startups", country_startups
    print "a_country", a_country
    paginator = Paginator(country_startups, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        country_strt = paginator.page(page)
    except PageNotAnInteger:
        country_strt = paginator.page(1)
    except EmptyPage:
        country_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'country':country_startups, 'a_country': a_country,
               'len_country':len_country, 'beta_promoted':promoted, 'country_strt':country_strt}
    return render(request, 'beta/country.html', context)

def west_africa(request):
    regions = Startup.objects.filter(pub_status='Published', region='West Africa').order_by('-pub_date')
    len_west = regions.count()
    paginator = Paginator(regions, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        west_africa_strt = paginator.page(page)
    except PageNotAnInteger:
        west_africa_strt = paginator.page(1)
    except EmptyPage:
        west_africa_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'west_african_regions': regions, 'len_region':len_west,
               'beta_promoted':promoted, 'west_africa_strt':west_africa_strt}
    return render(request, 'beta/west_africa.html', context)


def east_africa(request):
    regions = Startup.objects.filter(pub_status='Published', region='East Africa').order_by('-pub_date')
    len_east = regions.count()
    paginator = Paginator(regions, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        east_africa_strt = paginator.page(page)
    except PageNotAnInteger:
        east_africa_strt = paginator.page(1)
    except EmptyPage:
        east_africa_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'east_african_regions': regions, 'len_region':len_east,
               'beta_promoted':promoted, 'east_africa_strt':east_africa_strt}
    return render(request, 'beta/east_africa.html', context)


def north_africa(request):
    regions = Startup.objects.filter(pub_status='Published', region='North Africa').order_by('-pub_date')
    len_north = regions.count()
    paginator = Paginator(regions, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        north_africa_strt = paginator.page(page)
    except PageNotAnInteger:
        north_africa_strt = paginator.page(1)
    except EmptyPage:
        north_africa_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'north_african_regions': regions, 'len_region':len_north,
               'beta_promoted':promoted, 'north_africa_strt':north_africa_strt}
    return render(request, 'beta/north_africa.html', context)


def southern_africa(request):
    regions = Startup.objects.filter(pub_status='Published', region='South Africa').order_by('-pub_date')
    len_south = regions.count()
    paginator = Paginator(regions, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        southern_africa_strt = paginator.page(page)
    except PageNotAnInteger:
        southern_africa_strt = paginator.page(1)
    except EmptyPage:
        southern_africa_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'southern_african_regions': regions, 'len_region':len_south,
               'beta_promoted':promoted, 'southern_africa_strt':southern_africa_strt}
    return render(request, 'beta/southern_africa.html', context)


def central_africa(request):
    regions = Startup.objects.filter(pub_status='Published', region='Central Africa').order_by('-pub_date')
    len_central = regions.count()
    paginator = Paginator(regions, 60) #Show 20 reviews per page
    page = request.GET.get('page')
    try:
        central_africa_strt = paginator.page(page)
    except PageNotAnInteger:
        central_africa_strt = paginator.page(1)
    except EmptyPage:
        central_africa_strt = paginator.page(paginator.num_pages)
    promoted = Startup.objects.filter(pub_status='Published', promoted=True).order_by("?")[:4]
    context = {'central_african_regions': regions, 'len_region':len_central,
               'beta_promoted':promoted, 'central_africa_strt':central_africa_strt}
    return render(request, 'beta/central_africa.html', context)

def launching_this_week(request):
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    #entries = Entry.objects.filter(created_at__range=[start_week, end_week])
    this_week = Startup.objects.filter(launching__range=[start_week, end_week])
    context = {'this_week':this_week}
    return render(request, 'beta/launching.html', context)

@login_required
def startups(request):
    admin_startups = Startup.objects.all()
    #Paginations of all the startups
    page = request.GET.get('page')
    paginator = Paginator(admin_startups, 40) #Show 40 startups per page
    try:
        startups = paginator.page(page)
    except PageNotAnInteger:
        startups = paginator.page(1)
    except EmptyPage:
        startups = paginator.page(paginator.num_pages)
    context = {'admin_startups': startups}
    return render(request, 'beta/admin.html', context)

def status_search(request):
    admin_startups = Startup.objects.all()
    query = request.GET.get("status")
    print 'This is query', query
    if query:
        results = admin_startups.filter(pub_status=query)
    page = request.GET.get('page')
    paginator = Paginator(results, 40) #Show 40 startups per page
    try:
        startups = paginator.page(page)
    except PageNotAnInteger:
        startups = paginator.page(1)
    except EmptyPage:
        startups = paginator.page(paginator.num_pages)
    context = {"results": startups, 'query':query}
    return render(request, 'beta/admin_search.html', context)


def admin_search(request):
    admin_startups = Startup.objects.all()
    query = request.GET.get("query")
    if query:
        results = admin_startups.filter(Q(startup__icontains=query) |
                                          Q(category__icontains=query) |
                                          Q(startup_id__icontains=query) |
                                          Q(user__first_name__icontains=query) |
                                          Q(user__last_name__icontains=query))
        page = request.GET.get('page')
    paginator = Paginator(results, 40) #Show 40 startups per page
    try:
        startups = paginator.page(page)
    except PageNotAnInteger:
        startups = paginator.page(1)
    except EmptyPage:
        startups = paginator.page(paginator.num_pages)
    context = {"results":startups, 'query':query}
    return render(request, "beta/admin_search.html", context)

@login_required
def startup(request, startup_id):
    try:
        admin_startup = get_object_or_404(Startup, startup_id=startup_id)
    except ObjectDoesNotExist:
        admin_startup = None
    user_signups = admin_startup.signup_set.all()
    teams = admin_startup.team_set.all()
    len_signups = user_signups.count()
    if request.method == "GET":
        add_team_form = TeamForm()
    if request.method == "POST":
        add_team_admin = TeamForm(request.POST, request.FILES)
        if add_team_admin.is_valid():
            team = add_team_admin.save(commit=False)
            team.startup = admin_startup
            team.save()
            return redirect('beta:index')
        else:
            print add_team_form.errors
    context = {'admin_startup': admin_startup, 'len_signups':len_signups, 'teams': teams,
               'add_team_form':add_team_form}
    return render(request, 'beta/startup_admin.html', context)

def delete_signup(request, startup_id):
    try:
        del_signup = get_object_or_404(SignUp, id=startup_id)
    except ObjectDoesNotExist:
        del_signup = None
    del_signup.delete()
    return redirect('beta:startups')


@login_required
def edit_startup(request, startup_id):
    """This function submits beta startup"""
    if request.method == "POST":
        try:
            beta_user = get_object_or_404(Startup, startup_id=startup_id)
            submit_beta_form = SubmitStartupForm(request.POST, instance=beta_user)
        except ObjectDoesNotExis:
            submit_beta_form = SubmitStartupForm(request.POST, request.FILES)
    
        if submit_beta_form.is_valid():
            beta_form = submit_beta_form.save(commit=False)
            beta_form.user = request.user
            #beta_form.startup_id = beta_id
            beta_form.save()
            pub_stat = request.POST.get('pub_status')
            if pub_stat == "Published":
                print 'beta_user.user.email:', beta_user.user.email 
                plaintext = get_template('email_notifications/published.txt')
                html_text     = get_template('email_notifications/published.html')
                d = Context({'startup': beta_user.startup,
                 'logo': beta_user.logo,
                 'first_name': beta_user.user.first_name,
                 #'last_name': beta_user.user.last_name,
                 })
                subject = "Your startup " + beta_user.startup + " has been published"
                email = "uzoigweiroh@gmail.com"
                recipients = [beta_user.user.email,]
                text_content = plaintext.render(d)
                html_content = html_text.render(d)
                msg = EmailMultiAlternatives(subject, text_content, email, recipients)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            elif pub_stat == "Declined":
                print 'beta_user.user.email:', beta_user.user.email 
                plaintext = get_template('email_notifications/declined.txt')
                html_text     = get_template('email_notifications/declined.html')
                d = Context({'startup': beta_user.startup,
                 'logo': beta_user.logo,
                 'first_name': beta_user.user.first_name,
                 #'last_name': beta_user.user.last_name,
                 })
                subject = "Your startup " + beta_user.startup + " has been declined"
                email = "uzoigweiroh@gmail.com"
                recipients = [beta_user.user.email,]
                text_content = plaintext.render(d)
                html_content = html_text.render(d)
                msg = EmailMultiAlternatives(subject, text_content, email, recipients)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            # elif request.POST.get('approved'):
            #     print 'beta_user.user.email:', beta_user.user.email 
            #     plaintext = get_template('email_notifications/published.txt')
            #     html_text     = get_template('email_notifications/published.html')
            #     d = Context({'startup': beta_user.startup,
            #      'logo': beta_user.logo,
            #      'first_name': beta_user.user.first_name,
            #      'last_name': beta_user.user.last_name,})
            #     subject = "Your startup " + beta_user.startup + " has been approved"
            #     email = "uzoigweiroh@gmail.com"
            #     recipients = [beta_user.user.email,]
            #     text_content = plaintext.render(d)
            #     html_content = html_text.render(d)
            #     msg = EmailMultiAlternatives(subject, text_content, email, recipients)
            #     msg.attach_alternative(html_content, "text/html")
            #     msg.send()
                
            return redirect('beta:startups')
        else:
            print submit_beta_form.errors
    else:
        try:
            beta_user = get_object_or_404(Startup, startup_id=startup_id)
            submit_beta_form = SubmitStartupForm(instance=beta_user)
        except ObjectDoesNotExist:
            submit_beta_form = SubmitStartupForm(request.FILES)
        except ObjectDoesNotExist:
             submit_beta_form = None
    context = {'edit_beta': submit_beta_form, 'beta_user':beta_user}
    return render(request, 'beta/edit_startup.html', context)
@login_required
def submit_admin_beta(request):
    """This function submits beta startup"""
    if request.method == "POST":
        submit_beta_form = SubmitStartupForm(request.POST, request.FILES)
        if submit_beta_form.is_valid():
            beta_form = submit_beta_form.save(commit=False)
            beta_form.user = request.user
            beta_form.startup_id = beta_id()
            #beta_form.pub_status = "Pending"
            print 'startup_id:', beta_form.startup_id
            beta_form.status = 'Beta'
            #Populating tag field based on the category
            for tags in ONLINE_SHOPPING:
                if beta_form.category in tags:
                    beta_form.tag = "Online Shopping"
            for tags in ENTERTAINMENT:
                if beta_form.category in tags:
                    beta_form.tag = "Entertainment"
            for tags in FINSEC:
                if beta_form.category in tags:
                    beta_form.tag = "FINSEC"
            for tags in ENTERPRISE:
                if beta_form.category in tags:
                    beta_form.tag = "Enterprise"
            for tags in ON_DEMAND:
                if beta_form.category in tags:
                    beta_form.tag = "On Demand Services"
            for tags in SOCIAL_SERVICES:
                if beta_form.category in tags:
                    beta_form.tag = "Social Services"
            #Populating the regions
            for region in EAST_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "East Africa"
            for region in WEST_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "West Africa"
            for region in CENTRAL_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "Central Africa"
            for region in SOUTHERN_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "South Africa"
            for region in NORTHERN_AFRICA:
                if beta_form.country in region:
                    beta_form.region = "North Africa"
            beta_form.save()
            return redirect('beta:startups')
        else:
            print submit_beta_form.errors
    else:
        submit_beta_form = SubmitStartupForm()
    context = {'beta_form': submit_beta_form}
    return render(request, 'beta/submit_admin_beta.html', context)

def contact_us(request):
    """Conatct us form"""
    contacts = Info.objects.all()
    if request.method == "POST":
        contact_form = Contact_UsForm(request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            subject = request.POST.get('subject', '')
            email = request.POST.get ('email', '')
            message = request.POST.get('message', '')
            recipients = ["uzoigweiroh@gmail.com",]
            #send_mail(name, subject, email, message, recipients)
            send_mail(subject, message, email, recipients)

            return redirect("beta:index")
        else:
            print contact_form.errors
    else:
        contact_form = Contact_UsForm()
    context = {'contacts': contact_form, 'contact_info': contacts}
    return render(request, 'beta/contact_us.html', context)

def search(request):
    startups_results = Startup.objects.all()
    query = request.GET.get("q")
    if query:
        results = startups_results.filter(Q(startup__icontains=query) |
                                          Q(category__icontains=query)).exclude(status="Pending")
    context = {"results":results, 'query':query}
    return render(request, "beta/search.html", context)

def newsletter(request):
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            return redirect('beta:index')
        else:
            print newsletter_form.errors
    else:
        newsletter_form = NewsletterForm()
    return render(request, 'base.html', {'newsletter': newsletter_form})
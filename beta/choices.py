#All Choices goes in here
REGIONS= (
    ('North Africa', 'North Africa'),
    ('West Africa', 'West Africa'),
    ('Central Africa', 'Central Africa'),
    ('East Africa', 'East Africa'),
    ('South Africa', 'South Africa'),
)
AFRICAN_COUNTRIES = (
    
    ('Nigeria', 'Nigeria'),
    ('Algeria', 'Algeria'),
    ('Angola', 'Angola'),
    ('Benin', 'Benin'),
    ('Botswana', 'Botswana'),
    ('Burkina', 'Burkina'),
    ('Burundi', 'Burundi'),
    ('Cameroon', 'Cameroon'),
    ('Cape Verde', 'Cape Verde'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('Congo DRC', 'Congo DRC'),
    ('Djibouti', 'Djibouti'),
    ('Egypt', 'Egypt'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Ethiopia', 'Ethiopia'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Ghana', 'Ghana'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Ivory Coast', 'Ivory Coast'),
    ('Kenya', 'Kenya'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Mali', 'Mali'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('Niger', 'Niger'),
    ('Rwanda', 'Rwanda'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Senegal', 'Senegal'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Sudan', 'South Sudan'),
    ('Sudan', 'Sudan'),
    ('Swaziland', 'Swaziland'),
    ('Tanzania', 'Tanzania'),
    ('Togo', 'Togo'),
    ('Tunisia', 'Tunisia'),
    ('Uganda', 'Uganda'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
)

#Category choices for different startup Categories
caty = [
        " ",
        "E-Commerce", "Mobile Payment",
        "Social Media", "Advertising & Marketing", "Job",
        'Payments', 'Game', 'Betting', 
        'Web Development', 'Sports', 'Foods', 
        'Events', 'Fashion', 'Enterprise Software',
        'Agriculture', 'Auto', 'Real Estate', 'Health', 'Market Place', 
        'Deals', "Chat",
        "Shipping & Logistics","Fitness", "Travel & Hotels", 
        "Blog & Forum", "Dating",
        "Web Hosting", 
        "Government", 
        'Search',
        "Entertainment", "Media", 'Printing','Music & Video', 
        'On Demand Services', 'Education','Oil and Gas', 
        'Religion', 'NGO'
]
caty.sort()
CAT = [(i, i) for i in caty]

beta_stat = [
    " " ,
    "Under Development",
    'Private Beta',
    'Public Beta', 
    'Live', 
]
beta_stat.sort()
BETA_STATUS = [(i, i) for i in beta_stat]

RELATED_TAGS = (
        ("Online Shopping", "Online Shopping", ),
        # ("Jobs", "Jobs"),
        # ("News", "News"),
        # ("Financial Services", "Financial Services"),
        # ("Marketing And Advertising", "Marketing And Advertising",),
        # ("Social Media", "Social Media"),
        ("Entertainment","Entertainment"),
        ("Enterprise", "Enterprise"),
        # ("Travel And Tourism", "Travel And Tourism"),
        # ("Web Development", "Web Development"),
        # ("Logistics And Transportion","Logistics And Transportion"),
        # ("Foods", "Foods"),
        # ("Sports","Sports"),
        # ("Production","Production"),
        # ("Mobile", "Mobile"),
        # ("NGOS", "NGOS"),
        # ("Search", "Search"),
        # ("Automotive", "Automotive"),
        # ("Health", "Health"),
        # ("Education", "Education"),
        ("On Demand Services","On Demand Services"),
        ("FINSEC","FINSEC"),
        ("Social Services","Social Services"),
        # ("Properties", "Properties"),
        # ("ICT", "ICT"),
        # ("Consulting", "Consulting"),
        # ("Startups", "Startups"),
        # ("Reviews", "Reviews"),
        # ("Government", "Government"),
        # ("SMEs", "SMEs"),
        
    )

GENDER = (
    ('Male', 'male'),
    ('Female', 'Female'),
)

TARGETED_GENDER = (
    ('All', 'All'),
    ('Male', 'Male'),
    ('Female', 'Female'),
)

# BETA_STATUS = (
#     (" ", " " ),
#     ('Under Development', "Under Development"),
#     ('Private Beta', 'Private Beta'),
#     ('Public Beta', 'Public Beta'),
#     ('Live', 'Live'),
# )

TEAM_ROLE = (
    (" ", " "),
    ("Founder", 'Founder'),
    ("Co-Founder", "Co-Founder"),
    ('Team Member', 'Team Member'),
)

PUB_STATUS = (
    ('Pending', 'Pending'),
    ('Published', 'Published'),
    ('Declined', "Declined"),
)

STATUS = (
    (" ", " "),
    ('Under Development', 'Under Development'),
    ('Private Beta', 'Private Beta'),
    ('Public Beta', "Public Beta"),
    ('Live', 'Live')
)

INDUSTRY = (
    ('Tech', 'Tech'),
    ('Telecom', 'Telecom'),
    ('Entertainment', 'Entertainment'),
    ('Financial', 'Financial'),
    ('Student', 'Student'),
    ('Government', 'Government'),
    ('NGO', 'NGO'),
    ('Automobile', 'Automobile'),
    ('Religion', 'Religion'), 
)

ONLINE_SHOPPING = (
    'E-Commerce', 'Deals', 'Fashion',
    'Agriculture', 'Auto', 'Market Place',
    'Search', 
    )

ENTERTAINMENT = (
    "Social Media", 'Blog & Forum',
    "Entertainment", 'Sports', 'Music & Video', 'Chat',
    'Betting', 'Game', 'Dating', 'Media'
)

FINSEC = (
    'Mobile Payment', 'Payments', 
)

ENTERPRISE = (
    'Web Development', 'Enterprise Software', "Web Hosting",
    "Advertising & Marketing", 'Job'
)

ON_DEMAND = (
    'On Demand Services', 'Fitness', 'Printing', "Travel & Hotels",
    'Real Estate', 'Foods', 'Events', 'Shipping & Logistics', 'Oil and Gas',
)

SOCIAL_SERVICES = (
    "Government", 'Religion', 'Education', 'NGO', 'Health', 
)

WEST_AFRICA = (
    ('Nigeria', 'Nigeria'),
    ('Benin', 'Benin'),
    ('Burkina', 'Burkina'),
    ('Cape Verde', 'Cape Verde'),
    ('Chad', 'Chad'),
    ('Gambia', 'Gambia'),
    ('Ghana', 'Ghana'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Ivory Coast', 'Ivory Coast'),
    ('Liberia', 'Liberia'),
    ('Mali', 'Mali'),
    ('Mauritania', 'Mauritania'),
    ('Niger', 'Niger'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Senegal', 'Senegal'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Togo', 'Togo'),
)

EAST_AFRICA = (
    ('Burundi', 'Burundi'),
    ('Comoros', 'Comoros'),
    ('Ethiopia', 'Ethiopia'),
    ('Kenya', 'Kenya'),
    ('Rwanda', 'Rwanda'),
    ('Seychelles', 'Seychelles'),
    ('Somalia', 'Somalia'),
    ('Tanzania', 'Tanzania'),
    ('Uganda', 'Uganda'),
    ('Eritrea', 'Eritrea'),
)

SOUTHERN_AFRICA = (
    ('Angola', 'Angola'),
    ('Botswana', 'Botswana'),
    ('Lesotho', 'Lesotho'),
    ('Malawi', 'Malawi'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('South Africa', 'South Africa'),
    ('Swaziland', 'Swaziland'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Madagascar', 'Madagascar'),
)

CENTRAL_AFRICA = (
    ('Angola', 'Angola'),
    ('Cameroon', 'Cameroon'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Congo', 'Congo'),
    ('Congo DRC', 'Congo DRC'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Gabon', 'Gabon'),
)

NORTHERN_AFRICA = (
    ('Algeria', 'Algeria'),
    ('Egypt', 'Egypt'),
    ('Libya', 'Libya'),
    ('Morocco', 'Morocco'),
    ('South Sudan', 'South Sudan'),
    ('Sudan', 'Sudan'),
    ('Tunisia', 'Tunisia'),
)
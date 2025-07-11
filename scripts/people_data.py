"""
People Section Generator :: DATA PART  
v0.1

This file contains all data for generating the people section of the GenI-Lab site.  
It defines structured records for lab members, collaborators, and advisory boards,  
along with a catalog for ordered rendering.

Disclaimer:  
This script was 'vibe coded', a lightweight approach to quickly solving a specific need.  
The result has been revised and approved by a human.

###
### THIS IS THE DATA  
### Generated from GenI-Lab CONTROL + ChatGPT Script  
###     ChatGPT = 🤖
"""




# ===  People Groups ===

lab_members = [
    {
        "name": "Dr. Fernando Koch",
        "picture": "kochf.png",
        "link": "https://www.fau.edu/engineering/directory/faculty/koch/",
        "title": "Research Professor",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Natasha Astudillo, Ph.D CS (candidate)",
        "picture": "nastudillo2024.png",
        "link": "https://www.linkedin.com/in/natashaastudillo/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Gonzalo Vivian, Ph.D. CS (candidate)",
        "picture": "gvivian2022.png",
        "link": "https://www.linkedin.com/in/gonvivian/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Sam Porter, MBA, B.Sc. CS",
        "picture": "samanthaport2022.png",
        "link": "https://www.linkedin.com/in/samporter-cs/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Nelson Vega, M.Sc. CS",
        "picture": "vegan2023.png",
        "link": "https://www.linkedin.com/in/nvegamarrero/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Sumedh Krishna",
        "picture": "svizarsuyesh2024.png",
        "link": "https://www.linkedin.com/in/sumedh-vyk/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Amanda Grass Santos",
        "picture": "agrasssantos2023.png",
        "link": "https://www.linkedin.com/in/amandagrass",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Preet Chokshi",
        "picture": "pchokshi2024.png",
        "link": "https://www.linkedin.com/in/preet-chokshi-6b7096233",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Jeel Sathwara",
        "picture": "jsathwara2024.png",
        "link": "https://www.linkedin.com/in/jeel209/",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Deven Patel",
        "picture": "devenpravink2024.png",
        "link": "https://www.linkedin.com/in/devenpatel0",
        "title": "",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Rutvikkumar Dave",
        "picture": "rdave2024.png",
        "link": "https://www.linkedin.com/in/dave-rutvikkumar/",
        "title": "",
        "department": "Dept EECS, FAU"
    }
]

research_advisor_board = [
    {
        "name": "Dr. Borko Furht",
        "picture": "bfurht-headshot.png",
        "link": "https://www.fau.edu/engineering/directory/faculty/furht/",
        "title": "Professor and Director of NSF Research Center",
        "department": "Department of Electrial engineerign & Computer Sciences"
    },
    {
        "name": "Dr. Maria Mejia, M.D., M.P.H.",
        "picture": "mejiam-headshot.png",
        "link": "https://www.fau.edu/medicine/directory/maria-mejia/",
        "title": "Professor of Population Health and Social Medicine",
        "department": "Department: Population Health, Schmidt College of Medicine"
    }
]

research_collaborator = [
    {
        "name": "Dr. Ravi Behara",
        "picture": "rbehara.png",
        "link": "https://business.fau.edu/faculty-research/faculty-profiles/profile/rbehara.php",
        "title": "SBA Communications Professor",
        "department": "Department of Information Technology and Operations Management"
    },
    {
        "name": "Dr. Morgan Cooley, LCSW",
        "picture": "cooley-headshot.png",
        "link": "https://www.fau.edu/sw-cj/ssw/faculty-and-staff/people/cooley/",
        "title": "Associated Professor",
        "department": "Sandler School of Social Work"
    }
]

industry_collaborator = [
    {
        "name": "Michael Sorrenti",
        "picture": "msorrenti-headshot.png",
        "link": "https://www.linkedin.com/in/mike-sorrenti/?originalSubdomain=ca",
        "title": "President & Founder",
        "department": "Game Pill"
    },
    {
        "name": "Dr. Alecio Binotto",
        "picture": "abinotto-headshot.png",
        "link": "https://www.linkedin.com/in/aleciobinotto/?originalSubdomain=de",
        "title": "Digital Technologies Expert",
        "department": "ZEISS Corp"
    },
    {
        "name": "Boris Shulzhenko",
        "picture": "bshulzhenko-headshot.jpg",
        "link": "https://www.linkedin.com/in/boris-shulzhenko-94706764/",
        "title": "CEO",
        "department": "aiKOLO"
    }
]



# === Catalog of People Groups ===

catalog = [
    ("Lab Members", lab_members),
    ("Research Advisor Board", research_advisor_board),
    ("Industry Advisor Board", industry_collaborator),
    ("Research Collaborators", research_collaborator)
]
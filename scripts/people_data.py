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
###     ChatGPT = https://chatgpt.com/share/68715a9b-90dc-8002-b506-96798f5de037
"""




# ===  LAB MEMBERS ===

lab_members = [
    {
        "name": "Dr. Fernando Koch",
        "picture": "kochf-headshot.png",
        "link": "https://www.fau.edu/engineering/directory/faculty/koch/",
        "title": "Research Professor",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Natasha Astudillo",
        "picture": "nastudillo2024-headshot.png",
        "link": "https://www.linkedin.com/in/natashaastudillo/",
        "title": "Ph.D. CS (candidate)",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Gonzalo Vivian",
        "picture": "gvivian2022-headshot.png",
        "link": "https://www.linkedin.com/in/gonvivian/",
        "title": "Ph.D. CS (candidate)",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Sam Porter",
        "picture": "samanthaport2022-headshot.png",
        "link": "https://www.linkedin.com/in/samporter-cs/",
        "title": "MBA, B.Sc. CS (student)",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Nelson Vega",
        "picture": "vegan2023-headshot.png",
        "link": "https://www.linkedin.com/in/nvegamarrero/",
        "title": "M.Sc. CS",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Sumedh Krishna",
        "picture": "svizarsuyesh2024-headshot.png",
        "link": "https://www.linkedin.com/in/sumedh-vyk/",
        "title": "M.Sc. CS",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Amanda Grass Santos",
        "picture": "agrasssantos2023-headshot.png",
        "link": "https://www.linkedin.com/in/amandagrass",
        "title": "M.Sc. AI",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Preet Chokshi",
        "picture": "pchokshi2024-headshot.png",
        "link": "https://www.linkedin.com/in/preet-chokshi-6b7096233",
        "title": "M.Sc. CS",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Jeel Sathwara",
        "picture": "jsathwara2024-headshot.png",
        "link": "https://www.linkedin.com/in/jeel209/",
        "title": "M.Sc. CS",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Deven Patel",
        "picture": "devenpravink2024-headshot.png",
        "link": "https://www.linkedin.com/in/devenpatel0",
        "title": "M.Sc. CS",
        "department": "Dept EECS, FAU"
    },
    {
        "name": "Rutvikkumar Dave",
        "picture": "rdave2024-headshot.png",
        "link": "https://www.linkedin.com/in/dave-rutvikkumar/",
        "title": "M.Sc. DS",
        "department": "Dept EECS, FAU"
    }
]

# === COLLABORATORS ===

research_advisor_board = [
    {
        "name": "Dr. Borko Furht",
        "picture": "bfurht-headshot.png",
        "link": "https://www.fau.edu/engineering/directory/faculty/furht/",
        "title": "Professor and Director of NSF Research Center",
        "department": "Department of Electrical Engineering & Computer Sciences"
    },
    {
        "name": "Dr. Maria Mejia, M.D., M.P.H.",
        "picture": "mejiam-headshot.png",
        "link": "https://www.fau.edu/medicine/directory/maria-mejia/",
        "title": "Professor of Population Health and Social Medicine",
        "department": "Department: Population Health, Schmidt College of Medicine"
    },
    {
        "name": "Dr. Kevin Cox, MBA",
        "picture": "kcox24-headshot.png",
        "link": "https://business.fau.edu/faculty-research/faculty-profiles/profile/kcox24.php",
        "title": "Senior Instructor & Director",
        "department": "Adams Center for Entrepreneurship, College of Business"
    }
]

research_collaborator = [
    {
        "name": "Dr. Ravi Behara",
        "picture": "rbehara-headshot.png",
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
    },
    {
        "name": "Dr. Milad Baghersad",
        "picture": "mbaghersad-headshot.png",
        "link": "https://www.linkedin.com/in/miladbaghersad/",
        "title": "Associate Professor",
        "department": "Department of Information Technology and Operations Management"
    },
    {
        "name": "Dr. Sven Thijssen",
        "picture": "sthijssen-headshot.png",
        "link": "https://www.fau.edu/engineering/directory/faculty/thijssen/",
        "title": "Assistant Professor",
        "department": "Department of Electrical Engineering and Computer Science"
    },
    {
        "name": "Dr. Hannah Bowers Parker, LMFT",
        "picture": "bowersp-headshot.jpg",
        "link": "https://www.linkedin.com/in/hannah-bowers-parker-ph-d-lmft-029645121/",
        "title": "Associate Professor",
        "department": "Department of Counselor Education and Supervision"
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


##
## ENTRY POINT
##
if __name__ == "__main__":
    import people
    people.main()
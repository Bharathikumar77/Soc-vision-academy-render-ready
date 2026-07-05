#!/usr/bin/env python
"""Database seed script - Initialize with sample data"""
import json
from dotenv import load_dotenv

load_dotenv()

from app import create_app, db
from app.models import (
    User, UserProfile, LearningPath, Course, Lesson,
    InvestigationRoom, Question, QuestionOption, Evidence, IOC,
    Badge, Level, Leaderboard
)
from datetime import datetime, timedelta

def seed_database():
    """Populate database with initial data"""
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Creating admin user...")
        admin = User(
            username='admin',
            email='admin@socvision.com',
            first_name='Admin',
            last_name='User',
            is_admin=True,
            is_active=True
        )
        admin.set_password('Admin@123')
        db.session.add(admin)
        
        print("Creating test users...")
        users = []
        for i in range(5):
            user = User(
                username=f'analyst{i+1}',
                email=f'analyst{i+1}@example.com',
                first_name=f'Security',
                last_name=f'Analyst {i+1}',
                is_active=True
            )
            user.set_password('Password@123')
            users.append(user)
            db.session.add(user)
        
        db.session.commit()
        print(f"Created {len(users) + 1} users")
        
        # Create user profiles
        print("Creating user profiles...")
        for user in users:
            profile = UserProfile(
                user_id=user.id,
                bio=f"Security professional passionate about blue team operations",
                title="Security Analyst",
                organization="TechCorp Security",
                country="United States",
                years_of_experience=3 + users.index(user),
                specialization="Threat Hunting"
            )
            db.session.add(profile)
        db.session.commit()
        
        # Create learning paths
        print("Creating learning paths...")
        paths = [
            LearningPath(
                title="SOC Fundamentals",
                description="Learn the basics of Security Operations Center operations",
                difficulty="beginner",
                order=1
            ),
            LearningPath(
                title="Advanced Threat Analysis",
                description="Master advanced techniques in threat detection and analysis",
                difficulty="advanced",
                order=2
            )
        ]
        for path in paths:
            db.session.add(path)
        db.session.commit()
        
        # Create courses
        print("Creating courses...")
        course1 = Course(
            learning_path_id=paths[0].id,
            title="Introduction to SIEM",
            description="Understand SIEM architecture, log collection, and basic analysis",
            difficulty="beginner",
            order=1
        )
        course2 = Course(
            learning_path_id=paths[0].id,
            title="Log Analysis Basics",
            description="Learn how to parse, correlate, and analyze security logs",
            difficulty="beginner",
            order=2
        )
        course3 = Course(
            learning_path_id=paths[1].id,
            title="Advanced Threat Hunting",
            description="Proactive threat hunting methodologies and techniques",
            difficulty="advanced",
            order=1
        )
        db.session.add_all([course1, course2, course3])
        db.session.commit()
        
        # Create lessons
        print("Creating lessons...")
        lessons = [
            Lesson(
                course_id=course1.id,
                title="SIEM Architecture",
                content="<h5>Understanding SIEM</h5><p>A Security Information and Event Management (SIEM) system is...</p>",
                order=1
            ),
            Lesson(
                course_id=course1.id,
                title="Log Collection",
                content="<h5>Collecting Logs</h5><p>Log collection is the first step in SIEM...</p>",
                order=2
            ),
            Lesson(
                course_id=course2.id,
                title="Log Parsing",
                content="<h5>Parsing Logs</h5><p>Log parsing involves breaking down log entries...</p>",
                order=1
            ),
            Lesson(
                course_id=course3.id,
                title="Threat Intelligence",
                content="<h5>Threat Intelligence</h5><p>Understanding threat intelligence feeds and indicators...</p>",
                order=1
            )
        ]
        for lesson in lessons:
            db.session.add(lesson)
        db.session.commit()
        
        # Create investigation rooms
        print("Creating investigation rooms...")
        room1 = InvestigationRoom(
            title="Phishing Email Investigation",
            description="Analyze a phishing attack targeting employees",
            scenario="""<h5>Incident Report</h5>
            <p>On Monday morning, your SOC received multiple reports from employees about suspicious emails. 
            The emails appear to be from your company's HR department requesting password resets. 
            Your task is to investigate the authenticity of these emails and determine the scope of the attack.</p>
            
            <h5>Initial Observations</h5>
            <ul>
                <li>15 employees reported receiving the phishing emails</li>
                <li>3 employees clicked the malicious link</li>
                <li>Emails came from an external domain spoofing your company</li>
                <li>Timestamps show attack occurred between 8-9 AM</li>
            </ul>""",
            objectives=json.dumps([
                "Identify all affected employees",
                "Determine the phishing infrastructure used",
                "Extract IOCs for threat intelligence",
                "Provide containment recommendations"
            ]),
            difficulty="beginner",
            estimated_time=45,
            prerequisites=json.dumps(["Basic Email Security"]),
            category="Phishing",
            attack_vector="Email",
            industry="Finance",
            enterprise_description="""<h5>Environment</h5>
            <ul>
                <li>Organization: TechFinance Corp</li>
                <li>Email System: Microsoft Exchange 365</li>
                <li>Employees: 500</li>
                <li>Email Gateway: Proofpoint</li>
            </ul>""",
            incident_timeline=json.dumps([
                {"time": "08:05 AM", "event": "First phishing emails detected"},
                {"time": "08:45 AM", "event": "HR receives first employee complaint"},
                {"time": "09:00 AM", "event": "Incident escalated to SOC"},
                {"time": "09:30 AM", "event": "Email gateway quarantines remaining emails"}
            ]),
            mitre_attack_mapping=json.dumps(["T1566.002", "T1598.003", "T1598.001"]),
            defensive_recommendations="""<h5>Immediate Actions</h5>
            <ul>
                <li>Reset passwords for affected employees</li>
                <li>Block sender domain at email gateway</li>
                <li>Monitor for credential abuse</li>
            </ul>
            
            <h5>Long-term Improvements</h5>
            <ul>
                <li>Implement DMARC, SPF, and DKIM</li>
                <li>Deploy advanced email filtering</li>
                <li>Conduct phishing awareness training</li>
            </ul>""",
            xp_reward=100,
            is_active=True,
            is_featured=True
        )
        
        room2 = InvestigationRoom(
            title="Ransomware Attack Analysis",
            description="Investigate a ransomware deployment across network segments",
            scenario="""<h5>Incident Report</h5>
            <p>Your organization detected unusual file encryption activity on multiple servers. 
            Several critical business systems are now unavailable. Your SOC team needs to investigate 
            the infection vector, lateral movement, and scope of impact.</p>""",
            objectives=json.dumps([
                "Identify patient zero and infection vector",
                "Track lateral movement through the network",
                "Determine ransomware family and variant",
                "Estimate data exfiltration scope"
            ]),
            difficulty="intermediate",
            estimated_time=90,
            category="Ransomware",
            attack_vector="Email/RDP",
            industry="Healthcare",
            enterprise_description="""<h5>Environment</h5>
            <ul>
                <li>Organization: MediCare Hospital Network</li>
                <li>Infrastructure: Hybrid Cloud (AWS + On-Prem)</li>
                <li>Servers: 150+</li>
                <li>Backup System: Veeam</li>
            </ul>""",
            mitre_attack_mapping=json.dumps(["T1486", "T1491", "T1570", "T1021.001"]),
            xp_reward=250,
            is_active=True,
            is_featured=True
        )
        
        room3 = InvestigationRoom(
            title="APT Campaign Analysis",
            description="Advanced persistent threat with multi-stage infection",
            scenario="""<h5>Incident Report</h5>
            <p>MITRE detected attributed an advanced persistent threat targeting your organization. 
            Initial access was gained weeks ago, and multiple stages of compromise are suspected. 
            Your task is to uncover the full scope and timeline of the attack.</p>""",
            objectives=json.dumps([
                "Determine complete attack timeline",
                "Identify all affected systems and data",
                "Attribute to threat actor group",
                "Develop remediation strategy"
            ]),
            difficulty="advanced",
            estimated_time=180,
            category="APT",
            attack_vector="Supply Chain",
            industry="Technology",
            enterprise_description="""<h5>Environment</h5>
            <ul>
                <li>Organization: TechCorp International</li>
                <li>Employees: 5000+</li>
                <li>Data Centers: 3 Global</li>
                <li>EDR Solution: CrowdStrike Falcon</li>
            </ul>""",
            mitre_attack_mapping=json.dumps(["T1195.002", "T1566.001", "T1547.001", "T1021.006"]),
            xp_reward=500,
            is_active=True,
            is_featured=True
        )
        
        db.session.add_all([room1, room2, room3])
        db.session.commit()
        
        # Create questions for room1
        print("Creating investigation questions...")
        q1 = Question(
            room_id=room1.id,
            question_text="What is the sender email address used in the phishing attack?",
            question_type="short_answer",
            correct_answer="hr-reset@techfinance.net",
            points=10,
            hint="Check the email headers for the actual sender address",
            order=1
        )
        q2 = Question(
            room_id=room1.id,
            question_text="How many employees clicked the malicious link?",
            question_type="short_answer",
            correct_answer="3",
            points=10,
            order=2
        )
        q3 = Question(
            room_id=room1.id,
            question_text="What MITRE ATT&CK technique was used for this phishing attack?",
            question_type="multiple_choice",
            correct_answer="T1566.002",
            points=15,
            order=3
        )
        
        db.session.add_all([q1, q2, q3])
        db.session.flush()  # assign IDs to q1/q2/q3 before referencing q3.id below
        
        # Add options for multiple choice
        options = [
            QuestionOption(question_id=q3.id, option_text="T1566.001 - Phishing: Spearphishing Attachment", is_correct=False, order=1),
            QuestionOption(question_id=q3.id, option_text="T1566.002 - Phishing: Phishing Link", is_correct=True, order=2),
            QuestionOption(question_id=q3.id, option_text="T1598.003 - Phishing for Information: Spearphishing Link", is_correct=False, order=3),
            QuestionOption(question_id=q3.id, option_text="T1192 - Spearphishing Link", is_correct=False, order=4),
        ]
        for option in options:
            db.session.add(option)
        
        db.session.commit()
        
        # Create evidence files
        print("Creating evidence files...")
        evidence1 = Evidence(
            room_id=room1.id,
            filename="phishing_emails.eml",
            file_path="/evidence/phishing_emails.eml",
            file_type="eml",
            description="Raw email files from phishing campaign",
            size_mb=2.5,
            is_downloadable=True
        )
        evidence2 = Evidence(
            room_id=room1.id,
            filename="email_headers.csv",
            file_path="/evidence/email_headers.csv",
            file_type="csv",
            description="Email headers with sender information",
            size_mb=0.5,
            is_downloadable=True
        )
        db.session.add_all([evidence1, evidence2])
        
        # Create IOCs
        print("Creating indicators of compromise...")
        ioc1 = IOC(
            room_id=room1.id,
            ioc_type="domain",
            ioc_value="techfinance.net",
            severity="high",
            description="Spoofed company domain used in phishing"
        )
        ioc2 = IOC(
            room_id=room1.id,
            ioc_type="ip",
            ioc_value="192.168.1.100",
            severity="high",
            description="Malicious email server IP"
        )
        ioc3 = IOC(
            room_id=room1.id,
            ioc_type="url",
            ioc_value="http://techfinance.net/reset",
            severity="critical",
            description="Phishing link destination"
        )
        db.session.add_all([ioc1, ioc2, ioc3])
        db.session.commit()
        
        # Create badges
        print("Creating badges...")
        badges = [
            Badge(
                name="First Investigation",
                description="Complete your first investigation room",
                criteria="Complete any investigation room",
                badge_type="achievement",
                rarity="common"
            ),
            Badge(
                name="Phishing Expert",
                description="Complete all phishing-related investigations",
                criteria="Complete 5 phishing investigations",
                badge_type="achievement",
                rarity="rare"
            ),
            Badge(
                name="Ransomware Analyst",
                description="Investigate ransomware incidents",
                criteria="Complete 3 ransomware investigations",
                badge_type="achievement",
                rarity="rare"
            ),
            Badge(
                name="Level 10",
                description="Reach level 10",
                criteria="Earn 5000 XP",
                badge_type="milestone",
                rarity="epic"
            )
        ]
        for badge in badges:
            db.session.add(badge)
        db.session.commit()
        
        # Create levels
        print("Creating level progression...")
        for level_num in range(1, 21):
            level = Level(
                level_number=level_num,
                xp_required=level_num * 500,
                title=f"Level {level_num}",
                description=f"Security Analyst Level {level_num}"
            )
            db.session.add(level)
        db.session.commit()
        
        # Create leaderboards
        print("Creating leaderboard entries...")
        for i, user in enumerate(users):
            leaderboard = Leaderboard(
                user_id=user.id,
                total_xp=(i + 1) * 500,
                current_level=1 + i,
                rooms_completed=i + 1,
                accuracy_percentage=75.0 + (i * 5)
            )
            db.session.add(leaderboard)
        db.session.commit()
        
        print("\n✅ Database seeding completed successfully!")
        print("\n📝 Test Credentials:")
        print("   Admin:")
        print("   - Username: admin")
        print("   - Password: Admin@123")
        print("\n   Test Users:")
        for i in range(1, 6):
            print(f"   - Username: analyst{i}")
            print(f"     Password: Password@123")

if __name__ == '__main__':
    seed_database()

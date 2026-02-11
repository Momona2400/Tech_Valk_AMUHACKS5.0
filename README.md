# 🧭 Tech Valk – Personalized First-Semester Survival Guide

**AMUHACKS 5.0 Submission**

*#AMUHACKS5.0 #CSSAMU #CSDAMU #AMU*

## 🚨 Problem Statement

First-semester students often struggle to adapt to college life due to:

- Differences in schooling background
- Low or fluctuating confidence levels
- Unfamiliar academic structures
- Lack of personalized academic direction

A one-size-fits-all approach fails to support students with diverse needs.

## 💡 Proposed Solution

**Tech Valk** is a personalized survival guide platform built to help first-semester students transition smoothly into college life.

The system:
- Analyzes academic background
- Evaluates confidence levels
- Identifies course structure (B.Tech / B.Sc)
- Tracks mood and daily reflection

It then dynamically generates:
- 🎯 Adaptive daily quests
- 📊 Confidence visualization (Fuel System)
- 📚 Course-specific resources
- 🤖 AI-powered mentorship

**Our goal:** Transform uncertainty into structured growth.

## 🔄 Core Flow

1. 🔐 User logs into the platform
2. 📋 User completes onboarding questionnaire
3. 🧠 System builds a personalized student profile
4. 📊 Dashboard is generated with:
   - Confidence Fuel Indicator
   - Personalized Daily Quest
   - Mood-based Recommendations
   - Course-specific Resources
   - AI Mentor Chatbot

## 🧠 Key Features

### 📊 Confidence Fuel System
- Questionnaire score is converted into a fuel percentage
- Fuel band classification (Low / Medium / High)
- Encouragement adapts dynamically
- Fuel increases on quest completion

### 🎯 Adaptive Quest Engine
Quests are generated dynamically based on:
- Confidence Band
- Latest Mood Reflection

**Examples:**
- Low confidence + overwhelmed → Small 10-minute task
- Medium confidence → Participate in discussion
- High confidence → Lead discussion or apply to opportunities

### 📚 Course-Based Resource Allocation
Resources are filtered by:
- Course (B.Tech / B.Sc)
- Category (Videos / Notes / Articles)

Admin panel allows uploading:
- External links
- Study material
- Downloadable files

Students only see resources relevant to their course.

### 🪔 Daily Reflection System
- Select up to 3 moods
- Write short reflection
- Entries saved in database
- Expandable history panel
- Used to personalize quest recommendations

### 🤖 AI Mentor
- Integrated using HuggingFace Inference API
- Lightweight LLM model
- Smart fallback responses
- Context-based guidance
- Designed for confidence building and academic support

## 🏗 Tech Stack

### Backend
- Django
- SQLite (Development)
- HuggingFace API Integration

### Frontend
- HTML
- CSS (Custom Dark Themed UI)
- Vanilla JavaScript

### Security & Config
- CSRF Protection
- Login Required Dashboard
- Environment Variables for API Keys
- No Hardcoded Secrets

## 🛠 Admin Features
- Add and manage resources
- Filter resources by course and category
- Monitor questionnaire responses
- Track daily logs
- Manage platform data

## 🚀 Future Improvements
- Persistent AI memory
- Gamification levels & badges
- Faculty analytics dashboard
- Peer mentorship matching
- Production-grade LLM integration

## 👩‍💻 Hackathon Context
**Built for AMUHACKS 5.0**  
**Team:** Tech Valk

## 🎯 Vision

> *"Confidence is not inherited — it is built."*

Tech Valk aims to become a scalable adaptive support system for early college students, helping them grow with structured guidance instead of generic advice.

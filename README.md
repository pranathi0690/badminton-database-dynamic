 # 🏸 AI-Based Badminton Footwork Analysis

> **An End-to-End Computer Vision and Machine Learning Framework for Automated Badminton Footwork Analysis using YOLOv8, YOLOv9, MediaPipe Pose Estimation, Random Forest, and Streamlit Dashboard.**

---

## 📌 Overview

Badminton is one of the fastest racket sports, where efficient footwork directly influences player agility, balance, recovery, and overall match performance. Traditional player analysis relies heavily on manual observation by coaches, making the process subjective, time-consuming, and difficult to scale.

This project presents a complete AI-powered badminton analytics framework that automatically processes raw badminton match videos to detect players, estimate human pose, engineer movement-based features, classify badminton footwork, and generate interactive performance analytics through a Streamlit dashboard.

The entire pipeline is fully automated, transforming a raw badminton video into actionable player insights.

---

# 🚀 Features

- 🎥 Automatic frame extraction from badminton videos
- 🎯 Player detection using **YOLOv8** and **YOLOv9**
- 🧍 Human pose estimation using **MediaPipe Pose (33 Landmarks)**
- 📊 Custom badminton-specific feature engineering
- 🌲 Random Forest based footwork classification
- 📈 Automatic analytics generation
- 💾 SQLite database integration
- 📊 Interactive Streamlit dashboard
- ⚡ Complete end-to-end AI pipeline

---

# 🏗️ System Workflow

```text
Raw Badminton Video
        │
        ▼
Frame Extraction
(OpenCV)
        │
        ▼
Player Detection
(YOLOv8 / YOLOv9)
        │
        ▼
Pose Estimation
(MediaPipe)
        │
        ▼
Feature Engineering
• Stance Width
• Speed
• Smoothed Speed
• Recovery Distance
        │
        ▼
Random Forest
Footwork Classification
        │
        ▼
Predictions.csv
        │
        ▼
Analytics Generation
(JSON + SQLite)
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 📂 Project Structure

```text
badminton-dashboard/
│
├── app.py
├── styling.py
│
├── data/
│   ├── analytics.json
│   ├── landmarks.csv
│   ├── features.csv
│   ├── predictions.csv
│   ├── rf.pkl
│   └── sessions.db
│
├── video/
│   └── annotated_video.mp4
│
├── pipeline/
│   ├── run_pipeline.py
│
├── utils/
│   ├── session_utils.py
│   ├── visualization_utils.py
│   ├── db.py
│   ├── video_section.py
│   ├── upload_section.py
│   ├── court_section.py
│   ├── scoring_engine.py
│   ├── grade_engine.py
│   ├── performance_section.py
│   ├── alerts.py
│   ├── tactical_section.py
│   ├── identity_section.py
│   └── coach_report.py
```

---

# 🛠️ Technologies Used

| Category | Technologies |
|------------|------------------------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8, YOLOv9 (PyTorch) |
| Pose Estimation | MediaPipe Pose |
| Machine Learning | Random Forest (Scikit-Learn) |
| Feature Engineering | Custom Biomechanical Features |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Dashboard | Streamlit |
| Database | SQLite |

---

# 🧠 AI Models Used

## YOLOv8

- Player Detection
- Footwork Detection
- Bounding Box Generation

---

## YOLOv9

- Player Detection
- Footwork Detection
- Performance Comparison with YOLOv8

---

## MediaPipe Pose

MediaPipe extracts

- 33 Human Body Landmarks
- x-coordinate
- y-coordinate
- z-coordinate
- Visibility Score

These landmarks form the foundation for movement analysis.

---

## Random Forest

A Random Forest classifier is trained on engineered movement features extracted from MediaPipe landmarks.

Input Features

- Stance Width
- Speed
- Smoothed Speed
- Recovery Distance
- Landmark-based Features

Output

- Predicted Footwork Class

---

# 🏸 Footwork Classes

The model classifies the following badminton movements:

- Forehand Front
- Forehand Mid
- Forehand Backcourt
- Backhand Front
- Backhand Mid
- Backhand Backcourt
- Recovery Ready

---

# 📊 Model Performance

## YOLOv8

| Metric | Value |
|----------|-------:|
| Precision | **0.73** |
| Recall | **0.72** |
| mAP@0.5 | **0.75** |
| mAP@0.5:0.95 | **0.44** |

---

## YOLOv9

| Metric | Value |
|----------|-------:|
| Precision | **0.71** |
| Recall | **0.70** |
| mAP@0.5 | **0.71** |
| mAP@0.5:0.95 | **0.48** |

---

# 🌟 Project Highlights

- Complete end-to-end badminton analytics framework.
- Automated player detection from raw videos.
- Human pose estimation using MediaPipe.
- Custom biomechanical feature engineering.
- Random Forest-based footwork classification.
- YOLOv8 vs YOLOv9 comparative analysis.
- Automatic analytics generation.
- SQLite integration for data persistence.
- Interactive Streamlit dashboard for visualization.

---

# 🚀 Future Scope

- Multi-player tracking
- Shuttlecock detection
- Stroke classification
- Tactical movement analysis
- Real-time inference
- Cloud deployment
- Mobile application
- AI-based coaching recommendations

---

# 👨‍💻 Author

**A Sai Pranathi**

Artificial Intelligence & Machine Learning

---

⭐ **If you found this project useful, consider giving it a Star!**

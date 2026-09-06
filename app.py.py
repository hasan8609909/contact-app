import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Config
st.set_page_config(page_title="Contact Directory Service", layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Directory Service</title>
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-main: #f5efe6;
            --sidebar-bg: #e8ded1;
            --card-bg: #ffffff;
            --text-dark: #2c2c2c;
            --text-muted: #6c757d;
            --accent-teal: #4dd0e1;
            --btn-green: #20c997;
            --border-color: #e0d8cc;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-dark);
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar Styling */
        .sidebar {
            width: 240px;
            background-color: var(--sidebar-bg);
            padding: 20px 15px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 30px;
        }

        .brand i {
            font-size: 28px;
            color: #4a4a4a;
        }

        .brand-title {
            font-weight: 700;
            font-size: 16px;
        }

        .brand-subtitle {
            font-size: 12px;
            color: var(--text-muted);
        }

        .nav-menu {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .nav-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 16px;
            border-radius: 10px;
            cursor: pointer;
            color: #4a4a4a;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.2s;
        }

        .nav-item.active {
            background-color: #d8cbb9;
            color: #000;
            font-weight: 600;
        }

        .nav-item:hover:not(.active) {
            background-color: rgba(0, 0, 0, 0.05);
        }

        .sidebar-footer {
            background: #d8cbb9;
            padding: 15px;
            border-radius: 12px;
            margin-top: 20px;
            position: relative;
        }

        .sidebar-footer h4 {
            font-size: 14px;
            margin-bottom: 4px;
        }

        .sidebar-footer p {
            font-size: 11px;
            color: #555;
        }

        .sidebar-footer i {
            position: absolute;
            right: 12px;
            bottom: 12px;
            font-size: 16px;
            color: #4a4a4a;
        }

        /* Main Content Styling */
        .main-content {
            flex: 1;
            padding: 20px 30px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            gap: 15px;
        }

        .user-profile {
            display: flex;
            align-items: center;
            gap: 10px;
            background: #fff;
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        }

        .user-avatar {
            width: 30px;
            height: 30px;
            background-color: #007bff;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }

        /* Banner Hero */
        .banner {
            background: #ffffff;
            border-radius: 20px;
            padding: 25px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
            position: relative;
            overflow: hidden;
        }

        .banner-text h1 {
            font-size: 24px;
            color: #222;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .banner-text p {
            color: var(--text-muted);
            font-size: 14px;
            margin-bottom: 20px;
        }

        .search-bar {
            display: flex;
            align-items: center;
            background: #f8f6f0;
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 6px 15px;
            width: 450px;
        }

        .search-bar input {
            border: none;
            background: transparent;
            outline: none;
            padding: 6px;
            width: 100%;
            font-size: 13px;
        }

        .filter-tags {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .tag {
            padding: 5px 15px;
            background: #ede6da;
            border-radius: 15px;
            font-size: 12px;
            color: #4a4a4a;
            cursor: pointer;
            border: none;
        }

        .tag.active {
            background: #d8cbb9;
            font-weight: 600;
        }

        /* Layout Grid */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
        }

        /* Left Side: Contact List */
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .section-title {
            font-size: 16px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn-view-all {
            background: #ede6da;
            border: none;
            padding: 6px 14px;
            border-radius: 15px;
            font-size: 12px;
            cursor: pointer;
            font-weight: 600;
        }

        .contacts-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        .contact-card {
            background: #fff;
            border-radius: 15px;
            padding: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }

        .contact-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .contact-avatar {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            object-fit: cover;
        }

        .contact-details h4 {
            font-size: 14px;
            color: #222;
        }

        .contact-details p {
            font-size: 11px;
            color: var(--text-muted);
        }

        .status-dot {
            height: 8px;
            width: 8px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 4px;
        }

        .status-online { background-color: #28a745; }
        .status-offline { background-color: #dc3545; }

        .action-icons {
            display: flex;
            gap: 6px;
        }

        .icon-btn {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #f5efe6;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            color: #4a4a4a;
            cursor: pointer;
            border: none;
        }

        /* Right Side: Add Form */
        .add-card {
            background: #fff;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }

        .tab-menu {
            display: flex;
            gap: 15px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }

        .tab-item {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .tab-item.active {
            color: #000;
            border-bottom: 2px solid #000;
            padding-bottom: 8px;
        }

        .form-group {
            margin-bottom: 12px;
        }

        .form-group label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .form-group label span {
            color: red;
        }

        .form-input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            font-size: 12px;
            outline: none;
            background: #fafafa;
        }

        .btn-save {
            width: 100%;
            background: var(--accent-teal);
            color: #000;
            font-weight: 600;
            border: none;
            padding: 10px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 13px;
            margin-top: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        /* Quick Links Section (Updated with User Requested Links) */
        .quick-links {
            margin-top: 10px;
        }

        .quick-links-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 10px;
        }

        .link-card {
            background: #fff;
            padding: 12px 15px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            text-decoration: none;
            color: #333;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .link-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        .link-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .link-icon {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }

        .link-title {
            font-size: 13px;
            font-weight: 700;
            color: #222;
        }

        .link-url {
            font-size: 10px;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 130px;
        }

        /* Responsive Footer */
        .page-footer {
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid var(--border-color);
        }
    </style>
</head>
<body>

    <!-- Sidebar Navigation -->
    <div class="sidebar">
        <div>
            <div class="brand">
                <i class="fa-solid fa-users-gear"></i>
                <div>
                    <div class="brand-title">Contact Directory</div>
                    <div class="brand-subtitle">Service</div>
                </div>
            </div>

            <ul class="nav-menu">
                <li class="nav-item active"><i class="fa-solid fa-house"></i> Home</li>
                <li class="nav-item"><i class="fa-solid fa-user-group"></i> Contacts</li>
                <li class="nav-item"><i class="fa-solid fa-square-plus"></i> Add Contact</li>
                <li class="nav-item"><i class="fa-solid fa-border-all"></i> Categories</li>
                <li class="nav-item"><i class="fa-solid fa-heart"></i> Favorites</li>
                <li class="nav-item"><i class="fa-solid fa-gear"></i> Settings</li>
            </ul>
        </div>

        <div class="sidebar-footer">
            <h4>Stay Connected</h4>
            <p>Better Communication Builds Stronger Relationships</p>
            <i class="fa-solid fa-paper-plane"></i>
        </div>
    </div>

    <!-- Main Workspace -->
    <div class="main-content">

        <!-- Top Navigation Bar -->
        <div class="header">
            <i class="fa-regular fa-sun" style="cursor: pointer;"></i>
            <i class="fa-regular fa-bell" style="cursor: pointer;"></i>
            <div class="user-profile">
                <div class="user-avatar">MH</div>
                <span>Mehedi Hasan</span>
                <i class="fa-solid fa-chevron-down" style="font-size: 10px;"></i>
            </div>
        </div>

        <!-- Banner / Hero Section -->
        <div class="banner">
            <div class="banner-text">
                <h1><i class="fa-solid fa-users"></i> Contact Directory Service</h1>
                <p>Find, manage and stay connected with your contacts — anytime, anywhere.</p>
                
                <div class="search-bar">
                    <i class="fa-solid fa-magnifying-glass" style="color: #888;"></i>
                    <input type="text" placeholder="Search by name, phone, email or category...">
                    <i class="fa-solid fa-magnifying-glass" style="color: #333; cursor: pointer;"></i>
                </div>

                <div class="filter-tags">
                    <button class="tag active">All</button>
                    <button class="tag">Friends</button>
                    <button class="tag">Family</button>
                    <button class="tag">Work</button>
                    <button class="tag">Business</button>
                    <button class="tag">Others</button>
                </div>
            </div>
        </div>

        <!-- Dashboard Grid -->
        <div class="dashboard-grid">

            <!-- Recent Contacts Grid -->
            <div>
                <div class="section-header">
                    <div class="section-title">
                        <i class="fa-solid fa-user-group"></i> Recent Contacts
                    </div>
                    <button class="btn-view-all">View All <i class="fa-solid fa-arrow-right"></i></button>
                </div>

                <div class="contacts-grid">
                    <!-- Contact 1 -->
                    <div class="contact-card">
                        <div class="contact-info">
                            <img src="https://i.pravatar.cc/100?img=11" class="contact-avatar" alt="Avatar">
                            <div class="contact-details">
                                <h4>Mehedi Hasan</h4>
                                <p>Personal</p>
                                <p><span class="status-dot status-online"></span><span style="color: green; font-weight:600;">Online</span></p>
                                <p style="margin-top:2px; font-weight:600;">+880 1712 345678</p>
                            </div>
                        </div>
                        <div class="action-icons">
                            <button class="icon-btn"><i class="fa-solid fa-phone"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-comment"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-arrow-up-right-from-square"></i></button>
                        </div>
                    </div>

                    <!-- Contact 2 -->
                    <div class="contact-card">
                        <div class="contact-info">
                            <img src="https://i.pravatar.cc/100?img=5" class="contact-avatar" alt="Avatar">
                            <div class="contact-details">
                                <h4>Sadia Afrin</h4>
                                <p>Family</p>
                                <p><span class="status-dot status-offline"></span><span style="color: gray;">Offline</span></p>
                                <p style="margin-top:2px; font-weight:600;">+880 1687 654321</p>
                            </div>
                        </div>
                        <div class="action-icons">
                            <button class="icon-btn"><i class="fa-solid fa-phone"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-comment"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-arrow-up-right-from-square"></i></button>
                        </div>
                    </div>

                    <!-- Contact 3 -->
                    <div class="contact-card">
                        <div class="contact-info">
                            <img src="https://i.pravatar.cc/100?img=12" class="contact-avatar" alt="Avatar">
                            <div class="contact-details">
                                <h4>Rakib Ahmed</h4>
                                <p>Friend</p>
                                <p><span class="status-dot status-online"></span><span style="color: green; font-weight:600;">Online</span></p>
                                <p style="margin-top:2px; font-weight:600;">+880 1812 967654</p>
                            </div>
                        </div>
                        <div class="action-icons">
                            <button class="icon-btn"><i class="fa-solid fa-phone"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-comment"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-arrow-up-right-from-square"></i></button>
                        </div>
                    </div>

                    <!-- Contact 4 -->
                    <div class="contact-card">
                        <div class="contact-info">
                            <img src="https://i.pravatar.cc/100?img=13" class="contact-avatar" alt="Avatar">
                            <div class="contact-details">
                                <h4>Tanvir Islam</h4>
                                <p>Work</p>
                                <p><span class="status-dot status-offline"></span><span style="color: gray;">Offline</span></p>
                                <p style="margin-top:2px; font-weight:600;">+880 1911 223344</p>
                            </div>
                        </div>
                        <div class="action-icons">
                            <button class="icon-btn"><i class="fa-solid fa-phone"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-comment"></i></button>
                            <button class="icon-btn"><i class="fa-solid fa-arrow-up-right-from-square"></i></button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Add / Edit Contact Form -->
            <div class="add-card">
                <div class="tab-menu">
                    <div class="tab-item active"><i class="fa-solid fa-plus"></i> Add Contact</div>
                    <div class="tab-item"><i class="fa-solid fa-pen"></i> Edit Contact</div>
                    <div class="tab-item"><i class="fa-solid fa-upload"></i> Import</div>
                </div>

                <div class="form-group">
                    <label>Full Name <span>*</span></label>
                    <input type="text" class="form-input" placeholder="Enter full name">
                </div>

                <div class="form-group">
                    <label>Phone Number <span>*</span></label>
                    <input type="text" class="form-input" placeholder="+880 1XXX XXXXXX">
                </div>

                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" class="form-input" placeholder="example@domain.com">
                </div>

                <div class="form-group">
                    <label>Category</label>
                    <select class="form-input">
                        <option>Select category</option>
                        <option>Personal</option>
                        <option>Family</option>
                        <option>Work</option>
                        <option>Business</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>Notes (Optional)</label>
                    <textarea class="form-input" rows="2" placeholder="Add some notes..."></textarea>
                </div>

                <button class="btn-save"><i class="fa-solid fa-plus"></i> Save Contact</button>
            </div>
        </div>

        <!-- Quick Links Section (UPDATED LINKS) -->
        <div class="quick-links">
            <div class="section-header">
                <div class="section-title">
                    Quick Links <span style="font-size: 11px; font-weight: normal; color: #666; margin-left: 5px;">Useful external resources</span>
                </div>
                <button class="btn-view-all">View All <i class="fa-solid fa-chevron-right"></i></button>
            </div>

            <div class="quick-links-grid">
                <!-- Link 1 -->
                <a href="https://challanverification.finance.gov.bd/echalan/" target="_blank" class="link-card">
                    <div class="link-info">
                        <div class="link-icon" style="background-color: #e3f2fd; color: #0d47a1;">
                            <i class="fa-solid fa-file-invoice-dollar"></i>
                        </div>
                        <div>
                            <div class="link-title">চালান ভেরিফাই</div>
                            <div class="link-url">challanverification.finance.gov.bd</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 11px; color: #888;"></i>
                </a>

                <!-- Link 2 -->
                <a href="https://nbr.sblesheba.com/IncomeTax/Payment" target="_blank" class="link-card">
                    <div class="link-info">
                        <div class="link-icon" style="background-color: #e8f5e9; color: #1b5e20;">
                            <i class="fa-solid fa-credit-card"></i>
                        </div>
                        <div>
                            <div class="link-title">পেমেন্ট এনবিআর</div>
                            <div class="link-url">nbr.sblesheba.com</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 11px; color: #888;"></i>
                </a>

                <!-- Link 3 -->
                <a href="https://etaxnbr.gov.bd/#/auth/sign-in" target="_blank" class="link-card">
                    <div class="link-info">
                        <div class="link-icon" style="background-color: #fff3e0; color: #e65100;">
                            <i class="fa-solid fa-right-to-bracket"></i>
                        </div>
                        <div>
                            <div class="link-title">eReturn long</div>
                            <div class="link-url">etaxnbr.gov.bd</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 11px; color: #888;"></i>
                </a>

                <!-- Link 4 -->
                <a href="https://etaxnbr.gov.bd/#/submission-verification" target="_blank" class="link-card">
                    <div class="link-info">
                        <div class="link-icon" style="background-color: #f3e5f5; color: #4a148c;">
                            <i class="fa-solid fa-circle-check"></i>
                        </div>
                        <div>
                            <div class="link-title">eReturn verified</div>
                            <div class="link-url">etaxnbr.gov.bd</div>
                        </div>
                    </div>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 11px; color: #888;"></i>
                </a>
            </div>
        </div>

        <!-- Footer -->
        <div class="page-footer">
            <div>© 2025 Contact Directory Service. All rights reserved.</div>
            <div>Connect • Manage • Grow</div>
        </div>

    </div>

</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)

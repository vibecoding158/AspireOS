from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Aspire Demo – Mock Dashboard</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }

            body {
                background: #f3f4f6;
                color: #111827;
            }

            .app-shell {
                display: flex;
                min-height: 100vh;
            }

            /* SIDEBAR */

            .sidebar {
                width: 260px;
                background: #020617;
                color: #e5e7eb;
                padding: 16px 12px;
                display: flex;
                flex-direction: column;
            }

            .sidebar-logo-row {
                display: flex;
                align-items: center;
                margin-bottom: 24px;
            }

            .sidebar-logo-icon {
                width: 28px;
                height: 28px;
                border-radius: 999px;
                background: #22c55e;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 18px;
                font-weight: 700;
                color: #022c22;
                margin-right: 8px;
            }

            .sidebar-logo-text-main {
                font-weight: 700;
                font-size: 18px;
            }

            .sidebar-nav {
                margin-top: 8px;
                flex: 1;
                overflow-y: auto;
            }

            .sidebar-section-title {
                font-size: 11px;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                color: #6b7280;
                margin: 10px 8px 4px;
            }

            .sidebar-list {
                list-style: none;
            }

            .sidebar-item {
                display: flex;
                align-items: center;
                padding: 8px 10px;
                margin: 2px 4px;
                border-radius: 8px;
                font-size: 13px;
                cursor: pointer;
            }

            .sidebar-item-icon {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background: #0f172a;
                margin-right: 8px;
            }

            .sidebar-item:hover {
                background: rgba(55, 65, 81, 0.9);
            }

            .drop-target {
                border: 1px dashed rgba(226, 232, 240, 0.4);
                border-radius: 10px;
                padding: 4px 2px;
                transition: background 0.2s ease;
            }

            .drop-target.drag-over {
                background: rgba(59, 130, 246, 0.12);
            }

            .sidebar-footer {
                margin-top: 16px;
                font-size: 11px;
                color: #6b7280;
            }

            /* MAIN AREA */

            .main {
                flex: 1;
                display: flex;
                flex-direction: column;
                background: #f3f4f6;
            }

            .topbar {
                height: 54px;
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 20px;
                position: sticky;
                top: 0;
                z-index: 10;
            }

            .search-box {
                flex: 1;
                max-width: 540px;
                height: 32px;
                border-radius: 999px;
                border: 1px solid #e5e7eb;
                background: #f9fafb;
                font-size: 13px;
                padding: 0 14px;
                display: flex;
                align-items: center;
                color: #9ca3af;
            }

            .topbar-right {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-left: 16px;
            }

            .topbar-icon {
                width: 26px;
                height: 26px;
                border-radius: 999px;
                background: #f3f4f6;
            }

            .company-pill {
                display: flex;
                align-items: center;
                gap: 8px;
                padding: 4px 10px;
                background: #e0f2fe;
                border-radius: 999px;
                font-size: 12px;
            }

            .company-avatar {
                width: 24px;
                height: 24px;
                border-radius: 999px;
                background: #0ea5e9;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #eff6ff;
                font-weight: 600;
            }

            .content {
                padding: 18px 24px 40px;
            }

            .modules-wrapper {
                margin-bottom: -100px;
                overflow: visible;
            }

            .modules-section {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 12px;
                width: 133.3333%;
                transform: scale(0.75);
                transform-origin: top left;
            }

            .modules-column {
                background: #e2e8f0;
                border-radius: 16px;
                padding: 20px;
                border: 1px solid #cbd5f5;
            }

            .modules-column h2 {
                font-size: 24px;
                margin-bottom: 6px;
                color: #0f172a;
            }

            .modules-column p {
                font-size: 14px;
                color: #475467;
                margin-bottom: 20px;
            }

            .modules-grid {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 8px;
            }

            .module-card {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #dbeafe;
                padding: 14px;
                box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
                cursor: grab;
            }

            .module-card h3 {
                font-size: 15px;
                margin-bottom: 4px;
                color: #0f172a;
            }

            .module-card p {
                font-size: 13px;
                color: #475467;
            }

            .module-card.dragging {
                opacity: 0.6;
            }

            .hidden {
                display: none !important;
            }

            .addon-highlight {
                outline: 2px dashed #fb923c;
                outline-offset: 3px;
                box-shadow: 0 0 0 1px rgba(251, 146, 60, 0.35);
            }

            .addon-active-checking {
                border: 2px solid #22c55e !important; /* green */
                box-shadow: 0 0 0 1px rgba(34, 197, 94, 0.4);
            }

            .addon-active-smart {
                border: 2px solid #3b82f6 !important; /* blue */
                box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.4);
            }

            .addon-active-expense {
                border: 2px solid #f97316 !important; /* orange */
                box-shadow: 0 0 0 1px rgba(249, 115, 22, 0.4);
            }

            .hidden.preview-visible {
                display: block !important;
                opacity: 0.6;
            }

            /* TOP DASHBOARD SECTION */

            .row {
                display: grid;
                grid-template-columns: 2.1fr 1fr;
                gap: 16px;
                margin-bottom: 24px;
            }

            .panel {
                background: #ffffff;
                border-radius: 14px;
                box-shadow: 0 10px 25px rgba(15, 23, 42, 0.04);
                border: 1px solid #e5e7eb;
                padding: 16px 18px;
            }

            .panel-title {
                font-size: 15px;
                font-weight: 600;
                margin-bottom: 8px;
            }

            .chip-muted {
                font-size: 12px;
                color: #6b7280;
            }

            .actions-row {
                display: flex;
                gap: 10px;
                margin-top: 10px;
                overflow-x: auto;
                padding-bottom: 4px;
            }

            .action-pill {
                min-width: 120px;
                height: 70px;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                background: #f9fafb;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                font-size: 12px;
            }

            .action-pill-icon {
                width: 22px;
                height: 22px;
                border-radius: 999px;
                background: #1d4ed8;
                margin-bottom: 6px;
            }

            .tasks-wrapper {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .tasks-title {
                font-size: 13px;
                font-weight: 500;
            }

            .tasks-subtitle {
                font-size: 12px;
                color: #6b7280;
                margin-top: 4px;
            }

            .confetti {
                font-size: 40px;
            }

            .link {
                font-size: 12px;
                color: #2563eb;
                cursor: pointer;
            }

            /* ACCOUNTS */

            .accounts-panel {
                margin-top: 20px;
            }

            .accounts-header {
                font-size: 15px;
                font-weight: 600;
                margin-bottom: 8px;
            }

            .accounts-table {
                width: 100%;
                border-collapse: collapse;
                font-size: 13px;
                margin-top: 6px;
            }

            .accounts-table th,
            .accounts-table td {
                padding: 8px 4px;
            }

            .accounts-table tr:not(:last-child) {
                border-bottom: 1px solid #e5e7eb;
            }

            .currency-flag {
                width: 20px;
                height: 14px;
                border-radius: 2px;
                background: #e5e7eb;
                display: inline-block;
                margin-right: 6px;
            }

            .amount {
                text-align: right;
                font-weight: 500;
            }

            /* BUDGETS & CARDS SECTION */

            .section {
                margin-top: 26px;
            }

            .section-title-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .section-title {
                font-size: 15px;
                font-weight: 600;
            }

            .section-subtitle {
                font-size: 12px;
                color: #6b7280;
            }

            .section-link {
                font-size: 12px;
                color: #2563eb;
                cursor: pointer;
            }

            .budget-card {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                padding: 12px 14px;
                margin-bottom: 12px;
            }

            .budget-header-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 4px;
            }

            .budget-name {
                font-size: 13px;
                font-weight: 600;
            }

            .budget-status {
                font-size: 11px;
                padding: 2px 8px;
                border-radius: 999px;
                background: #dcfce7;
                color: #166534;
            }

            .budget-meta {
                font-size: 11px;
                color: #6b7280;
                margin-bottom: 8px;
            }

            .budget-bar-bg {
                width: 100%;
                height: 6px;
                border-radius: 999px;
                background: #e5e7eb;
                overflow: hidden;
            }

            .budget-bar-fill {
                height: 100%;
                width: 91%;
                background: #22c55e;
            }

            .budget-footer-row {
                display: flex;
                justify-content: space-between;
                font-size: 11px;
                margin-top: 6px;
            }

            /* Cards list */

            .cards-list-header {
                font-size: 13px;
                font-weight: 600;
                margin-bottom: 8px;
            }

            .card-line {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                padding: 10px 14px;
                margin-bottom: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-size: 13px;
            }

            .card-left-title {
                font-weight: 500;
            }

            .card-left-meta {
                font-size: 11px;
                color: #6b7280;
            }

            .card-amount-meta {
                font-size: 11px;
                color: #6b7280;
            }

            /* Recent transactions */

            .transactions-panel {
                background: #ffffff;
                border-radius: 14px;
                border: 1px solid #e5e7eb;
                padding: 16px 18px;
            }

            .transaction-row {
                display: flex;
                justify-content: space-between;
                margin-bottom: 10px;
                font-size: 13px;
            }

            .transaction-meta {
                font-size: 11px;
                color: #6b7280;
            }

            .amount-pos {
                color: #16a34a;
            }

            .amount-neg {
                color: #dc2626;
            }

            @media (max-width: 1100px) {
                .row {
                    grid-template-columns: 1fr;
                }
            }

            @media (max-width: 800px) {
                .app-shell {
                    flex-direction: column;
                }
                .sidebar {
                    width: 100%;
                    flex-direction: row;
                    overflow-x: auto;
                    height: auto;
                }
            }
        </style>
    </head>
    <body>
        <div class="app-shell">
            <!-- SIDEBAR -->
            <aside class="sidebar">
                <div>
                    <div class="sidebar-logo-row">
                        <div class="sidebar-logo-text-main">Company X</div>
                    </div>
                </div>

                <div class="sidebar-nav">
                    <div class="sidebar-section-title">Main</div>
                    <ul class="sidebar-list drop-target" id="main-nav-list">
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Home</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Funds</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Advance limit</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Transactions</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Payroll</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Analytics</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Referrals</span>
                        </li>
                    </ul>

                    <div class="sidebar-section-title">Spending</div>
                    <ul class="sidebar-list drop-target" id="spending-nav-list">
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Cards</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Bills</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Claims</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Invoices</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Payment links</span>
                        </li>
                    </ul>

                    <div class="sidebar-section-title">Admin</div>
                    <ul class="sidebar-list">
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Accounting services</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Users</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Policies</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Rewards</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Statements and Exports</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Integrations</span>
                        </li>
                        <li class="sidebar-item">
                            <div class="sidebar-item-icon"></div>
                            <span>Premium</span>
                        </li>
                    </ul>
                </div>

                <div class="sidebar-footer">
                    Aspire demo UI – static mock for client walkthrough.
                </div>
            </aside>

            <!-- MAIN -->
            <main class="main">
                <header class="topbar">
                    <div class="search-box">
                        Hi Zella, search for anything here
                    </div>
                    <div class="topbar-right">
                        <div class="topbar-icon"></div>
                        <div class="topbar-icon"></div>
                        <div class="topbar-icon"></div>
                        <div class="company-pill">
                            <div class="company-avatar">K</div>
                            <span>Koffee Brown Company · Admin</span>
                        </div>
                    </div>
                </header>

                <div class="content">
                    <div class="modules-wrapper">
                        <section class="modules-section" id="modules-section">
                        <div class="modules-column">
                            <div style="font-size:12px; text-transform:uppercase; color:#0ea5e9; letter-spacing:0.08em; margin-bottom:4px;">Banking</div>
                            <h2>Banking</h2>
                            <p>A comprehensive suite empowering banks to manage B2B financial services seamlessly.</p>
                            <div class="modules-grid">
                                <div class="module-card" draggable="true" data-module="onboarding">
                                    <h3>Onboarding</h3>
                                    <p>Streamlined process to efficiently integrate new business clients.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="checking">
                                    <h3>Checking &amp; Saving</h3>
                                    <p>Flexible account options tailored for business financial needs.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="smart-cards">
                                    <h3>Smart Cards Management</h3>
                                    <p>Centralized control for issuing and managing smart cards.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="payments-mgmt">
                                    <h3>Payments Management</h3>
                                    <p>Stablecoins-ready tools for secure and efficient payments.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="credit">
                                    <h3>Credit</h3>
                                    <p>Tailored credit solutions to support growth and liquidity.</p>
                                </div>
                            </div>
                        </div>
                        <div class="modules-column">
                            <div style="font-size:12px; text-transform:uppercase; color:#0ea5e9; letter-spacing:0.08em; margin-bottom:4px;">Powered by AI</div>
                            <h2>FinOS</h2>
                            <p>An integrated financial operating system powered by AI.</p>
                            <div class="modules-grid">
                                <div class="module-card" draggable="true" data-module="accounts-payable">
                                    <h3>Accounts Payable</h3>
                                    <p>Automated management of outgoing payments for efficiency.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="accounts-receivable">
                                    <h3>Accounts Receivable</h3>
                                    <p>Streamlined tracking and collection of incoming payments.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="accounting">
                                    <h3>Accounting</h3>
                                    <p>Real-time financial tracking and reporting for accurate insights.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="payroll">
                                    <h3>Payroll Management</h3>
                                    <p>Simplified payroll processing for seamless employee payments.</p>
                                </div>
                                <div class="module-card" draggable="true" data-module="expense">
                                    <h3>Expense Management</h3>
                                    <p>Real-time employee expense tracking and reconciliation.</p>
                                </div>
                            </div>
                        </div>
                        </section>
                    </div>
                    <!-- TOP ROW: Frequently used actions + Pending tasks -->
                    <div class="row">
                        <div class="panel">
                            <div class="panel-title">Frequently used actions</div>
                            <div class="chip-muted">Quick shortcuts for your day-to-day tasks.</div>
                            <div class="actions-row">
                                <div class="action-pill">
                                    <div class="action-pill-icon"></div>
                                    <div>Make a transfer</div>
                                </div>
                                <div class="action-pill hidden" id="issue-card-pill">
                                    <div class="action-pill-icon"></div>
                                    <div>Issue a card</div>
                                </div>
                                <div class="action-pill">
                                    <div class="action-pill-icon"></div>
                                    <div>Make batch payment</div>
                                </div>
                                <div class="action-pill">
                                    <div class="action-pill-icon"></div>
                                    <div>Get account statement</div>
                                </div>
                                <div class="action-pill">
                                    <div class="action-pill-icon"></div>
                                    <div>Send an invoice</div>
                                </div>
                            </div>
                        </div>

                        <div class="panel">
                            <div class="tasks-wrapper">
                                <div>
                                    <div class="tasks-title">0 Pending tasks</div>
                                    <div class="tasks-subtitle">Ta-da! All tasks conquered!</div>
                                    <div style="margin-top:8px;" class="link">View all actions</div>
                                </div>
                                <div class="confetti">🎉</div>
                            </div>
                        </div>
                    </div>

                    <!-- ACCOUNTS SECTION -->
                    <div class="panel accounts-panel hidden" id="accounts-panel">
                        <div class="accounts-header">Accounts</div>
                        <table class="accounts-table">
                            <tr>
                                <th align="left">Account</th>
                                <th></th>
                                <th class="amount">Balance</th>
                            </tr>
                            <tr>
                                <td>
                                    <span class="currency-flag"></span>SGD Account
                                </td>
                                <td>885215873732</td>
                                <td class="amount">SGD 2,382,690.09</td>
                            </tr>
                            <tr>
                                <td>
                                    <span class="currency-flag"></span>USD
                                </td>
                                <td>GB69TCCL12345623712371</td>
                                <td class="amount">USD 1,250,736.29</td>
                            </tr>
                            <tr>
                                <td>
                                    <span class="currency-flag"></span>Advance limit
                                </td>
                                <td></td>
                                <td class="amount">SGD 411,441.04</td>
                            </tr>
                            <tr>
                                <td>
                                    <span class="currency-flag"></span>EUR account
                                </td>
                                <td>GB01TCCL67869771400602</td>
                                <td class="amount">EUR 150,000.00</td>
                            </tr>
                        </table>
                    </div>

                    <!-- BUDGETS SECTION -->
                    <section class="section hidden" id="budgets-section">
                        <div class="section-title-row">
                            <div class="section-title">Budgets you own</div>
                            <div class="section-link">View all</div>
                        </div>

                        <div class="budget-card">
                            <div class="budget-header-row">
                                <div class="budget-name">Ops – Q1 2025</div>
                                <div class="budget-status">Active</div>
                            </div>
                            <div class="budget-meta">
                                91% spent · You're Budget Owner
                            </div>
                            <div class="budget-bar-bg">
                                <div class="budget-bar-fill"></div>
                            </div>
                            <div class="budget-footer-row">
                                <span>SGD 9,050.00 Spent</span>
                                <span>SGD 950.00 Remaining</span>
                            </div>
                        </div>

                        <div class="budget-card">
                            <div class="budget-header-row">
                                <div class="budget-name">Marketing X</div>
                                <div class="budget-status">Active</div>
                            </div>
                            <div class="budget-meta">
                                You're Budget Owner
                            </div>
                            <div class="budget-bar-bg">
                                <div class="budget-bar-fill" style="width:0.1%;"></div>
                            </div>
                            <div class="budget-footer-row">
                                <span>SGD 10.00 Spent</span>
                                <span>SGD 74,990.00 Remaining this quarter</span>
                            </div>
                        </div>

                        <div class="budget-card">
                            <div class="budget-header-row">
                                <div class="budget-name">Advance payments – US Expansion</div>
                                <div class="budget-status">Active</div>
                            </div>
                            <div class="budget-meta">
                                You're Budget Owner
                            </div>
                            <div class="budget-bar-bg">
                                <div class="budget-bar-fill" style="width:15%;"></div>
                            </div>
                            <div class="budget-footer-row">
                                <span>SGD 150.00 Spent this month</span>
                                <span>SGD 850.00 Remaining this month</span>
                            </div>
                        </div>
                    </section>

                    <!-- CARDS SECTION -->
                    <section class="section hidden" id="cards-section">
                        <div class="section-title-row">
                            <div class="section-title">Your cards</div>
                            <div class="section-link">View all</div>
                        </div>

                        <div class="card-line">
                            <div>
                                <div class="card-left-title">Trip to Beijing</div>
                                <div class="card-left-meta">Project Bravo · Zella Monahan</div>
                            </div>
                            <div class="card-amount-meta">
                                SGD 0.00 spent · SGD 10,000.00/mo remaining this month
                            </div>
                        </div>

                        <div class="card-line">
                            <div>
                                <div class="card-left-title">Navattic – Product Spend</div>
                                <div class="card-left-meta">Zella Monahan</div>
                            </div>
                            <div class="card-amount-meta">
                                USD 0.00 · No limit set
                            </div>
                        </div>
                    </section>

                    <!-- RECENT TRANSACTIONS -->
                    <section class="section">
                        <div class="section-title-row">
                            <div class="section-title">Recent transactions</div>
                            <div class="section-link">View all</div>
                        </div>

                        <div class="transactions-panel">
                            <div class="transaction-row">
                                <div>
                                    <div>Purdy-Boyer</div>
                                    <div class="transaction-meta">Tue, 25 Nov 2025</div>
                                </div>
                                <div class="amount-pos">+ SGD 500.00</div>
                            </div>

                            <div class="transaction-row">
                                <div>
                                    <div>Future Generali Insurance</div>
                                    <div class="transaction-meta">Thu, 13 Nov 2025</div>
                                </div>
                                <div class="amount-neg">– SGD 8,800.00</div>
                            </div>

                            <div class="transaction-row">
                                <div>
                                    <div>rachl</div>
                                    <div class="transaction-meta">Tue, 11 Nov 2025</div>
                                </div>
                                <div class="amount-neg">– SGD 250.00</div>
                            </div>

                            <div class="transaction-row">
                                <div>
                                    <div>test</div>
                                    <div class="transaction-meta">Fri, 31 Oct 2025</div>
                                </div>
                                <div class="amount-neg">– SGD 100.00</div>
                            </div>
                        </div>
                    </section>
                </div>
            </main>
        </div>
    </body>
    <script>
        (function () {
            const grids = document.querySelectorAll(".modules-grid");
            const modulesSection = document.getElementById("modules-section");
            const mainNavList = document.getElementById("main-nav-list");
            const spendingNavList = document.getElementById("spending-nav-list");
            const accountsPanel = document.getElementById("accounts-panel");
            const issueCardPill = document.getElementById("issue-card-pill");
            const cardsSection = document.getElementById("cards-section");
            const budgetsSection = document.getElementById("budgets-section");
            let draggedCard = null;
            let draggedModuleKey = null;
            let draggedSource = null; // 'modules' | 'sidebar'
            let checkingLinked = false;
            let smartLinked = false;
            let expenseLinked = false;

            const clearPreviews = () => {
                const previewTargets = [
                    accountsPanel,
                    issueCardPill,
                    cardsSection,
                    budgetsSection,
                    mainNavList,
                    spendingNavList,
                ];
                previewTargets.forEach((el) => {
                    if (!el) return;
                    el.classList.remove("addon-highlight", "preview-visible");
                });
            };

            const showPreviewsForModule = (moduleKey) => {
                clearPreviews();
                if (moduleKey === "checking") {
                    if (accountsPanel) {
                        accountsPanel.classList.add("preview-visible", "addon-highlight");
                    }
                    if (mainNavList) {
                        mainNavList.classList.add("addon-highlight");
                    }
                } else if (moduleKey === "smart-cards") {
                    if (issueCardPill) {
                        issueCardPill.classList.add("preview-visible", "addon-highlight");
                    }
                    if (cardsSection) {
                        cardsSection.classList.add("preview-visible", "addon-highlight");
                    }
                    if (spendingNavList) {
                        spendingNavList.classList.add("addon-highlight");
                    }
                } else if (moduleKey === "expense") {
                    if (budgetsSection) {
                        budgetsSection.classList.add("preview-visible", "addon-highlight");
                    }
                    if (spendingNavList) {
                        spendingNavList.classList.add("addon-highlight");
                    }
                }
            };

            const getDragAfterElement = (container, y) => {
                const cards = [...container.querySelectorAll(".module-card:not(.dragging)")];
                return cards.reduce(
                    (closest, child) => {
                        const box = child.getBoundingClientRect();
                        const offset = y - (box.top + box.height / 2);
                        if (offset < 0 && offset > closest.offset) {
                            return { offset, element: child };
                        }
                        return closest;
                    },
                    { offset: Number.NEGATIVE_INFINITY, element: null }
                ).element;
            };

            grids.forEach((grid) => {
                grid.addEventListener("dragstart", (event) => {
                    const card = event.target.closest(".module-card");
                    if (!card) return;
                    draggedCard = card;
                    draggedModuleKey = card.dataset.module || null;
                    draggedSource = "modules";
                    card.classList.add("dragging");
                    event.dataTransfer.effectAllowed = "move";
                    event.dataTransfer.setData("text/plain", card.dataset.module || "");
                    if (draggedModuleKey) {
                        showPreviewsForModule(draggedModuleKey);
                    }
                });

                grid.addEventListener("dragover", (event) => {
                    if (!draggedCard) return;
                    event.preventDefault();
                    const afterElement = getDragAfterElement(grid, event.clientY);
                    if (afterElement == null) {
                        grid.appendChild(draggedCard);
                    } else {
                        grid.insertBefore(draggedCard, afterElement);
                    }
                });

                grid.addEventListener("drop", (event) => {
                    event.preventDefault();
                });

                grid.addEventListener("dragend", () => {
                    if (draggedCard) {
                        draggedCard.classList.remove("dragging");
                    }
                    clearPreviews();
                    draggedCard = null;
                    draggedModuleKey = null;
                    draggedSource = null;
                });
            });

            const handleCheckingUnlinked = () => {
                checkingLinked = false;
                if (accountsPanel) {
                    accountsPanel.classList.add("hidden");
                    accountsPanel.classList.remove("addon-active-checking");
                }
                if (mainNavList) {
                    const linkedItem = mainNavList.querySelector('[data-linked-module="checking"]');
                    if (linkedItem) {
                        linkedItem.remove();
                    }
                }
                if (modulesSection) {
                    const checkingCard = modulesSection.querySelector('[data-module="checking"]');
                    if (checkingCard) {
                        checkingCard.classList.remove("hidden");
                    }
                }
            };

            const handleSmartUnlinked = () => {
                smartLinked = false;
                if (issueCardPill) {
                    issueCardPill.classList.add("hidden");
                    issueCardPill.classList.remove("addon-active-smart");
                }
                if (cardsSection) {
                    cardsSection.classList.add("hidden");
                    cardsSection.classList.remove("addon-active-smart");
                }
                if (spendingNavList) {
                    const linkedItem = spendingNavList.querySelector('[data-linked-module="smart-cards"]');
                    if (linkedItem) {
                        linkedItem.remove();
                    }
                }
                if (modulesSection) {
                    const smartCard = modulesSection.querySelector('[data-module="smart-cards"]');
                    if (smartCard) {
                        smartCard.classList.remove("hidden");
                    }
                }
            };

            const handleExpenseUnlinked = () => {
                expenseLinked = false;
                if (budgetsSection) {
                    budgetsSection.classList.add("hidden");
                    budgetsSection.classList.remove("addon-active-expense");
                }
                if (spendingNavList) {
                    const linkedItem = spendingNavList.querySelector('[data-linked-module="expense"]');
                    if (linkedItem) {
                        linkedItem.remove();
                    }
                }
                if (modulesSection) {
                    const expenseCard = modulesSection.querySelector('[data-module="expense"]');
                    if (expenseCard) {
                        expenseCard.classList.remove("hidden");
                    }
                }
            };

            const handleCheckingLinked = () => {
                if (checkingLinked || !accountsPanel) return;
                checkingLinked = true;
                accountsPanel.classList.remove("hidden");
                accountsPanel.classList.add("addon-active-checking");

                if (modulesSection) {
                    const checkingCard = modulesSection.querySelector('[data-module="checking"]');
                    if (checkingCard) {
                        checkingCard.classList.add("hidden");
                    }
                }
                if (!mainNavList.querySelector('[data-linked-module="checking"]')) {
                    const li = document.createElement("li");
                    li.className = "sidebar-item";
                    li.setAttribute("data-linked-module", "checking");
                    li.setAttribute("draggable", "true");
                    const icon = document.createElement("div");
                    icon.className = "sidebar-item-icon";
                    li.appendChild(icon);
                    const label = document.createElement("span");
                    label.textContent = "Checking & Saving";
                    li.appendChild(label);
                    mainNavList.appendChild(li);

                    li.addEventListener("dragstart", (event) => {
                        draggedCard = null;
                        draggedModuleKey = "checking";
                        draggedSource = "sidebar";
                        event.dataTransfer.effectAllowed = "move";
                        event.dataTransfer.setData("text/plain", "checking");
                    });

                    li.addEventListener("dragend", () => {
                        draggedCard = null;
                        draggedModuleKey = null;
                        draggedSource = null;
                    });
                }
            };

            const handleSmartLinked = () => {
                if (smartLinked) return;
                smartLinked = true;
                if (issueCardPill) {
                    issueCardPill.classList.remove("hidden");
                    issueCardPill.classList.add("addon-active-smart");
                }
                if (cardsSection) {
                    cardsSection.classList.remove("hidden");
                    cardsSection.classList.add("addon-active-smart");
                }
                if (modulesSection) {
                    const smartCard = modulesSection.querySelector('[data-module="smart-cards"]');
                    if (smartCard) {
                        smartCard.classList.add("hidden");
                    }
                }
                if (spendingNavList && !spendingNavList.querySelector('[data-linked-module="smart-cards"]')) {
                    const li = document.createElement("li");
                    li.className = "sidebar-item";
                    li.setAttribute("data-linked-module", "smart-cards");
                    li.setAttribute("draggable", "true");
                    const icon = document.createElement("div");
                    icon.className = "sidebar-item-icon";
                    li.appendChild(icon);
                    const label = document.createElement("span");
                    label.textContent = "Smart Cards Management";
                    li.appendChild(label);
                    spendingNavList.appendChild(li);

                    li.addEventListener("dragstart", (event) => {
                        draggedCard = null;
                        draggedModuleKey = "smart-cards";
                        draggedSource = "sidebar";
                        event.dataTransfer.effectAllowed = "move";
                        event.dataTransfer.setData("text/plain", "smart-cards");
                    });

                    li.addEventListener("dragend", () => {
                        draggedCard = null;
                        draggedModuleKey = null;
                        draggedSource = null;
                    });
                }
            };

            const handleExpenseLinked = () => {
                if (expenseLinked) return;
                expenseLinked = true;
                if (budgetsSection) {
                    budgetsSection.classList.remove("hidden");
                    budgetsSection.classList.add("addon-active-expense");
                }
                if (modulesSection) {
                    const expenseCard = modulesSection.querySelector('[data-module="expense"]');
                    if (expenseCard) {
                        expenseCard.classList.add("hidden");
                    }
                }
                if (spendingNavList && !spendingNavList.querySelector('[data-linked-module="expense"]')) {
                    const li = document.createElement("li");
                    li.className = "sidebar-item";
                    li.setAttribute("data-linked-module", "expense");
                    li.setAttribute("draggable", "true");
                    const icon = document.createElement("div");
                    icon.className = "sidebar-item-icon";
                    li.appendChild(icon);
                    const label = document.createElement("span");
                    label.textContent = "Expense Management";
                    li.appendChild(label);
                    spendingNavList.appendChild(li);

                    li.addEventListener("dragstart", (event) => {
                        draggedCard = null;
                        draggedModuleKey = "expense";
                        draggedSource = "sidebar";
                        event.dataTransfer.effectAllowed = "move";
                        event.dataTransfer.setData("text/plain", "expense");
                    });

                    li.addEventListener("dragend", () => {
                        draggedCard = null;
                        draggedModuleKey = null;
                        draggedSource = null;
                    });
                }
            };

            if (mainNavList) {
                ["dragover", "dragenter"].forEach((eventName) => {
                    mainNavList.addEventListener(eventName, (event) => {
                        if (!draggedModuleKey || draggedSource !== "modules") return;
                        event.preventDefault();
                        mainNavList.classList.add("drag-over");
                    });
                });

                mainNavList.addEventListener("dragleave", () => {
                    mainNavList.classList.remove("drag-over");
                });

                mainNavList.addEventListener("drop", (event) => {
                    event.preventDefault();
                    mainNavList.classList.remove("drag-over");
                    if (draggedModuleKey === "checking" && draggedSource === "modules") {
                        handleCheckingLinked();
                    }
                    clearPreviews();
                    draggedCard = null;
                    draggedModuleKey = null;
                    draggedSource = null;
                });
            }

            if (spendingNavList) {
                ["dragover", "dragenter"].forEach((eventName) => {
                    spendingNavList.addEventListener(eventName, (event) => {
                        if (!draggedModuleKey) return;
                        event.preventDefault();
                        spendingNavList.classList.add("drag-over");
                    });
                });

                spendingNavList.addEventListener("dragleave", () => {
                    spendingNavList.classList.remove("drag-over");
                });

                spendingNavList.addEventListener("drop", (event) => {
                    event.preventDefault();
                    spendingNavList.classList.remove("drag-over");
                    if (draggedSource === "modules" && draggedModuleKey === "smart-cards") {
                        handleSmartLinked();
                    } else if (draggedSource === "modules" && draggedModuleKey === "expense") {
                        handleExpenseLinked();
                    } else if (draggedSource === "sidebar" && draggedModuleKey === "expense") {
                        // Dropped back into Spending from sidebar: treat as unlink
                        handleExpenseUnlinked();
                    }
                    clearPreviews();
                    draggedCard = null;
                    draggedModuleKey = null;
                    draggedSource = null;
                });
            }

            if (modulesSection) {
                ["dragover", "dragenter"].forEach((eventName) => {
                    modulesSection.addEventListener(eventName, (event) => {
                        if (!draggedModuleKey || draggedSource !== "sidebar") return;
                        event.preventDefault();
                    });
                });

                modulesSection.addEventListener("drop", (event) => {
                    event.preventDefault();
                    if (draggedModuleKey === "checking" && draggedSource === "sidebar") {
                        handleCheckingUnlinked();
                    } else if (draggedModuleKey === "smart-cards" && draggedSource === "sidebar") {
                        handleSmartUnlinked();
                    } else if (draggedModuleKey === "expense" && draggedSource === "sidebar") {
                        handleExpenseUnlinked();
                    }
                    clearPreviews();
                    draggedCard = null;
                    draggedModuleKey = null;
                    draggedSource = null;
                });
            }

            // ensure accounts hidden if not linked
            if (!checkingLinked && accountsPanel) {
                accountsPanel.classList.add("hidden");
            }
        })();
    </script>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)


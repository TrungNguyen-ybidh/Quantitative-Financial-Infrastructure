fmp_endpoints = [
    # --- Company Profile --- 
    {
        "endpoint": "profile",
        "params": {}

    },

    # --- Quote ---
    {
        "endpoint": "quote",
        "params": {}
    },

     {
        "endpoint": "quote-short",
        "params": {}
    },

    # --- Core Statements ---
    {
        "endpoint": "income-statement",
        "params": {"period": "quarter", "limit": 30}
    },
    {
        "endpoint": "balance-sheet-statement",
        "params": {"period": "quarter", "limit": 30}
    },
    {
        "endpoint": "cash-flow-statement",
        "params": {"period": "quarter", "limit": 30}
    },

    # --- Metrics & Ratios ---
    {
        "endpoint": "key-metrics",
        "params": {"limit": 30}
    },
    {
        "endpoint": "ratios",
        "params": { "limit": 30}
    },
    {
        "endpoint": "key-metrics-ttm",
        "params": {}
    },
    {
        "endpoint": "ratios-ttm",
        "params": {}
    },

     {
        "endpoint": "financial-scores",
        "params": {}
    },

    # --- Valuation ---
    {
        "endpoint": "enterprise-values",
        "params": {"period": "annual", "limit": 30}
    },
    {
        "endpoint": "discounted-cash-flow",
        "params": {}
    },
    {
        "endpoint": "levered-discounted-cash-flow",
        "params": {}
    },

    # --- Growth ---
    {
        "endpoint": "income-statement-growth",
        "params": {"period": "annual", "limit": 30}
    },
    {
        "endpoint": "balance-sheet-statement-growth",
        "params": {"period": "annual", "limit": 30}
    },
    {
        "endpoint": "cash-flow-statement-growth",
        "params": {"period": "annual", "limit": 30}
    },
    {
        "endpoint": "financial-growth",
        "params": {"period": "annual", "limit": 30}
    },

    # --- Segmentation ---
    {
        "endpoint": "revenue-product-segmentation",
        "params": {"period": "annual", "limit": 30}
    },
    {
        "endpoint": "revenue-geographic-segmentation",
        "params": {"period": "annual", "limit": 30}
    },

    # --- Dividends ---
    {
        "endpoint": "dividends",
        "params": {"limit": 20}
    },

    # --- Analyst --- 
     {
        "endpoint": "analyst-estimates",
        "params": {"period": "annual", "limit": 10, "page":0}
    },

     {
        "endpoint": "ratings-snapshot",
        "params": {}
    },
     {
        "endpoint": "ratings-historical",
        "params": {"limit": 1}
    },
]
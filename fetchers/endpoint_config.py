fmp_endpoints = [
    # --- Core Statements ---
    {
        "endpoint": "income-statement",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "balance-sheet-statement",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "cash-flow-statement",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },

    # --- TTM ---
    {
        "endpoint": "income-statement-ttm",
        "params": {}
    },
    {
        "endpoint": "balance-sheet-statement-ttm",
        "params": {}
    },
    {
        "endpoint": "cash-flow-statement-ttm",
        "params": {}
    },

    # --- Metrics & Ratios ---
    {
        "endpoint": "key-metrics",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "ratios",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "key-metrics-ttm",
        "params": {}
    },
    {
        "endpoint": "ratios-ttm",
        "params": {}
    },

    # --- Valuation ---
    {
        "endpoint": "enterprise-values",
        "params": {"period": "annual", "limit": 10, "page": 0}
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
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "balance-sheet-statement-growth",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "cash-flow-statement-growth",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "financial-growth",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },

    # --- Segmentation ---
    {
        "endpoint": "revenue-product-segmentation",
        "params": {"period": "annual", "limit": 10}
    },
    {
        "endpoint": "revenue-geographic-segmentation",
        "params": {"period": "annual", "limit": 10}
    },

    # --- As Reported ---
    {
        "endpoint": "income-statement-as-reported",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "balance-sheet-statement-as-reported",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "cash-flow-statement-as-reported",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },
    {
        "endpoint": "financial-statement-full-as-reported",
        "params": {"period": "annual", "limit": 10, "page": 0}
    },

    # --- Other ---
    {
        "endpoint": "latest-financial-statements",
        "params": {"page": 0, "limit": 250}
    },
    {
        "endpoint": "dividends",
        "params": {"limit": 10}
    },
]
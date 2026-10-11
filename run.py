"""
Bankism Server Launcher
Starts the Bankism Defensive AI Firewall & Banking Execution Gateway.
"""

import sys
import uvicorn

if __name__ == "__main__":
    print("=" * 70)
    print(" [DEFENSE] BANKISM DEFENSIVE AI FIREWALL (v1.0.0-PROD)")
    print(" Blue-Team AI Gateway & Banking Execution Security Boundary")
    print("=" * 70)
    print(" Local Dashboard:  http://127.0.0.1:8000")
    print(" REST API Docs:    http://127.0.0.1:8000/docs")
    print(" Status:           FAIL-CLOSED FIREWALL ONLINE")
    print("=" * 70)
    
    uvicorn.run(
        "bankism.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

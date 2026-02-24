from processing.metrics_calculator import credit_risk_metrics

def test_credit_metrics():
    print("Testing Credit Risk Metrics...")
    
    # Case 1: Healthy Company
    print("\nCase 1: Healthy Company")
    healthy = credit_risk_metrics(
        ebitda=1000,
        interest_expense=100,
        total_debt=2000,
        cash=500,
        current_assets=1000,
        current_liabilities=500,
        free_cash_flow=400,
        capex=100,
        short_term_debt=50
    )
    print(f"Score: {healthy.value}/4")
    print(f"Interpretation: {healthy.interpretation}")
    print(f"Data: {healthy.components}")
    print(f"Flags: {healthy.flags}")
    
    # Case 2: Distressed Company
    print("\nCase 2: Distressed Company")
    distressed = credit_risk_metrics(
        ebitda=100,
        interest_expense=120, # Interest > EBITDA
        total_debt=1000,
        cash=50,
        current_assets=200,
        current_liabilities=300,
        free_cash_flow=-50, # Burning cash
        capex=20,
        short_term_debt=100
    )
    print(f"Score: {distressed.value}/4")
    print(f"Interpretation: {distressed.interpretation}")
    print(f"Data: {distressed.components}")
    print(f"Flags: {distressed.flags}")

if __name__ == "__main__":
    test_credit_metrics()

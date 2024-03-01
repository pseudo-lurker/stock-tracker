from .celery import app

@app.task
def check_stock_prices():
    print("This is a periodic task to check prices.")

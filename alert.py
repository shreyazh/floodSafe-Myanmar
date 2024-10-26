import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#alert System
def send_alert(prediction):
    if prediction == 1:  # High flood risk condition
        # Configuring email details
        email = "xyz@email.com"
        password = "12345"
        send_to = ["MyanmarGov_official@email.com", "Myanmar_Media_Inc@gmail.com"]
        
        # Creating email content
        subject = "Flood Alert: High Risk Detected"
        body = "A high flood risk has been detected in the region. Immediate action is recommended."
        
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = ", ".join(send_to)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Sending the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to, text)
            server.quit()
            print("Alert sent successfuly")
        except Exception as e:
            print(f"Failed to send alert: {e}")


# Prediction function
def predict_and_alert():
    model = load_model()
    
    while True:
        data = fetch_meteorology_data()
        prediction = model.predict(data)[0]  # Predict flood risk (1 for high, 0 for low)
        if prediction == 1:
            send_alert(prediction)
        
        time.sleep(3600)  # variable time, we took 60x60 seconds(every hour)

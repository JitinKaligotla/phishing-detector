import streamlit as st # type: ignore
import joblib # type: ignore

# Load the model and vectorizer
model = joblib.load('Url_phishing.pkl')
vectorizer = joblib.load('url_VECtorizer.pkl')

# Streamlit UI
st.title("Phishing URL Detector 🔒")
st.write("Enter a URL to check whether it's a phishing website.")

# URL input
url_input = st.text_input("Enter URL", "")

# Prediction
if st.button("Check"):
    if url_input.strip() == "":
        st.warning("Please enter a URL.")
    else:
        # Vectorize the input URL
        vectorized_url = vectorizer.transform([url_input])
        
        # Predict using the loaded model
        prediction = model.predict(vectorized_url)[0]

        # Show result
        if prediction == 1:
            st.error("🚨 This URL is likely **phishing**.")
        else:
            st.success("✅ This URL seems **safe**.")

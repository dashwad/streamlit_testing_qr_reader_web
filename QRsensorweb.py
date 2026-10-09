import streamlit as st
import numpy as np
import cv2

camera = st.camera_input("Camera")
QRdetection = cv2.QRCodeDetector()


while True:
    if camera:
        bit_data = camera.getvalue()
        base_numpy_array = np.frombuffer(bit_data, np.uint8)
        cv2_image = cv2.imdecode(base_numpy_array, cv2.IMREAD_COLOR_RGB)

        st.image(cv2_image, "PhotoCopied")

        data,_ ,_ = QRdetection.detectAndDecode(cv2_image)

        if data == "":
            st.header("No QR code was detected")

        else:
            st.header(f"QR data: {data}")
        break

cv2.destroyAllWindows()

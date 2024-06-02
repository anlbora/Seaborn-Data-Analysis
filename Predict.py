from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QLabel, QScrollArea, QVBoxLayout, QWidget, QPushButton, QFormLayout
import joblib
import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
class Predict(QMainWindow):

    def __init__(self, column_names, column_max_min_values):
        super(Predict, self).__init__()
        self.column_names = column_names
        self.column_max_min_values = column_max_min_values
        self.inputs = {}
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Predict")
        self.resize(300, 600)
        self.setMinimumSize(QtCore.QSize(300, 600))
        self.setMaximumSize(QtCore.QSize(300, 950))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowTitle("Prediction")

        # Scroll Area
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(10, 10, 280, 500))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        # Scroll Area Widget Contents
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 260, 480))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")

        # Layout for the scroll area widget contents
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget_contents)
        self.scroll_area_layout.setObjectName("scroll_area_layout")

        # Form Layout
        self.dataLayout = QFormLayout()
        self.dataLayout.setObjectName("dataLayout")
        self.scroll_area_layout.addLayout(self.dataLayout)

        # Set the scroll area widget contents
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        # Predict Button
        self.btn_predict = QPushButton(self.centralwidget)
        self.btn_predict.setGeometry(QtCore.QRect(10, 520, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_predict.setFont(font)
        self.btn_predict.setObjectName("btn_predict")
        self.btn_predict.setText("Predict")
        self.btn_predict.clicked.connect(self.predict)

        # Random Button
        self.btn_random = QPushButton(self.centralwidget)
        self.btn_random.setGeometry(QtCore.QRect(160, 520, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_random.setFont(font)
        self.btn_random.setObjectName("btn_random")
        self.btn_random.setText("Random")
        self.btn_random.clicked.connect(self.fill_random_values)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.populateForm()

    def populateForm(self):
        for column_name in self.column_names:
            label = QLabel(column_name)
            line_edit = QLineEdit()
            self.dataLayout.addRow(label, line_edit)
            self.inputs[column_name] = line_edit

    def load_model(self):
        """
        Load the trained Random Forest model from a file.

        Returns:
            model_disc (RandomForestRegressor/RandomForestClassifier): The loaded Random Forest model.
        """
        try:
            model_disc = joblib.load("rf_model.pkl")
            return model_disc
        except Exception as e:
            QMessageBox.warning(None, "Error", f"An error occurred while loading the model: {e}")
            return None

    def fill_random_values(self):
        """
        Fill the input fields with random values for testing.
        """
        for column_name, value_type in self.column_max_min_values.items():
            if value_type == "boolean":
                random_value = random.choice([0, 1])
            else:
                random_value = random.randint(int(value_type["Min Value"]), int(value_type["Max Value"]))
            self.inputs[column_name].setText(str(random_value))

    def predict(self):
        try:
            # Extract input values from the form
            input_data = []
            for column_name in self.column_names:
                value = self.inputs[column_name].text()
                if value == "":
                    raise ValueError(f"Value for {column_name} is missing.")
                input_data.append(float(value))

            # Load the model
            model_disc = self.load_model()
            if model_disc is None:
                raise ValueError("Model could not be loaded.")

            # Prepare the input data for prediction
            input_data_df = pd.DataFrame([input_data], columns=self.column_names)
            predictions = model_disc.predict(input_data_df)

            # Determine if the model is a classifier or regressor
            if isinstance(model_disc, RandomForestClassifier):
                prediction_text = f"Prediction: {round(predictions[0])}"
            else:
                prediction_text = f"Prediction: {round(predictions[0])}"

            # Display the prediction result in a message box
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Prediction Results")
            msg_box.setText(prediction_text)
            msg_box.setModal(True)
            msg_box.exec_()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    column_names = ["Column1", "Column2", "Column3"]  # Example column names
    PredictWindow = Predict(column_names)
    PredictWindow.show()
    sys.exit(app.exec_())

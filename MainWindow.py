from PyQt5 import QtCore, QtGui, QtWidgets
import seaborn as sns
import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QVBoxLayout, QLabel, QGraphicsView, QApplication, QFileDialog
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import numpy as np

import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x: "%.4f" % x)


class Ui_MainWindow(object):

    def __init__(self):
        self.dataFrame = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1090, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1090, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(11, 12, 291, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_data_name = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_data_name.sizePolicy().hasHeightForWidth())
        self.txt_data_name.setSizePolicy(sizePolicy)
        self.txt_data_name.setObjectName("txt_data_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_data_name)
        self.txt_head_number = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_head_number.sizePolicy().hasHeightForWidth())
        self.txt_head_number.setSizePolicy(sizePolicy)
        self.txt_head_number.setObjectName("txt_head_number")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.txt_head_number)
        self.btn_tail = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tail.sizePolicy().hasHeightForWidth())
        self.btn_tail.setSizePolicy(sizePolicy)
        self.btn_tail.setObjectName("btn_tail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.btn_tail)
        self.btn_head = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_head.sizePolicy().hasHeightForWidth())
        self.btn_head.setSizePolicy(sizePolicy)
        self.btn_head.setObjectName("btn_head")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_head)
        self.btn_shape = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_shape.sizePolicy().hasHeightForWidth())
        self.btn_shape.setSizePolicy(sizePolicy)
        self.btn_shape.setObjectName("btn_shape")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.btn_shape)
        self.txt_shape = QtWidgets.QLineEdit(self.groupBox)
        self.txt_shape.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_shape.sizePolicy().hasHeightForWidth())
        self.txt_shape.setSizePolicy(sizePolicy)
        self.txt_shape.setObjectName("txt_shape")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_shape)
        self.btn_data_types = QtWidgets.QPushButton(self.groupBox)
        self.btn_data_types.setObjectName("btn_data_types")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.btn_data_types)
        self.btn_none_values = QtWidgets.QPushButton(self.groupBox)
        self.btn_none_values.setObjectName("btn_none_values")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.btn_none_values)
        self.btn_data_information = QtWidgets.QPushButton(self.groupBox)
        self.btn_data_information.setObjectName("btn_data_information")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.btn_data_information)
        self.btn_data_describe = QtWidgets.QPushButton(self.groupBox)
        self.btn_data_describe.setObjectName("btn_data_describe")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.btn_data_describe)
        self.btn_load_data = QtWidgets.QPushButton(self.groupBox)
        self.btn_load_data.setObjectName("btn_load_data")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_load_data)
        self.chkBox_data = QtWidgets.QCheckBox(self.groupBox)
        self.chkBox_data.setObjectName("chkBox_data")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chkBox_data)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 23, 251, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.btn_FillNoneValues = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_FillNoneValues.setObjectName("btn_FillNoneValues")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_FillNoneValues)
        self.btn_Encode = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Encode.setObjectName("btn_Encode")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_Encode)
        self.txt_TargetName = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_TargetName.setObjectName("txt_TargetName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.txt_TargetName)
        self.btn_RFModel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_RFModel.setObjectName("btn_RFModel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btn_RFModel)
        self.chk_SaveModel = QtWidgets.QCheckBox(self.layoutWidget)
        self.chk_SaveModel.setObjectName("chk_SaveModel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chk_SaveModel)
        self.btn_Predict = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Predict.sizePolicy().hasHeightForWidth())
        self.btn_Predict.setSizePolicy(sizePolicy)
        self.btn_Predict.setObjectName("btn_Predict")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btn_Predict)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ckBox_summary_plot = QtWidgets.QCheckBox(self.groupBox)
        self.ckBox_summary_plot.setObjectName("ckBox_summary_plot")
        self.horizontalLayout.addWidget(self.ckBox_summary_plot)
        self.txt_summary_name = QtWidgets.QLineEdit(self.groupBox)
        self.txt_summary_name.setObjectName("txt_summary_name")
        self.horizontalLayout.addWidget(self.txt_summary_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.btn_num_summary = QtWidgets.QPushButton(self.groupBox)
        self.btn_num_summary.setObjectName("btn_num_summary")
        self.verticalLayout_3.addWidget(self.btn_num_summary)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ckBox_plot_target = QtWidgets.QCheckBox(self.groupBox)
        self.ckBox_plot_target.setObjectName("ckBox_plot_target")
        self.horizontalLayout_2.addWidget(self.ckBox_plot_target)
        self.txt_target_summary_name = QtWidgets.QLineEdit(self.groupBox)
        self.txt_target_summary_name.setObjectName("txt_target_summary_name")
        self.horizontalLayout_2.addWidget(self.txt_target_summary_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.txt_target = QtWidgets.QLineEdit(self.groupBox)
        self.txt_target.setObjectName("txt_target")
        self.verticalLayout_5.addWidget(self.txt_target)
        self.btn_target_summary = QtWidgets.QPushButton(self.groupBox)
        self.btn_target_summary.setObjectName("btn_target_summary")
        self.verticalLayout_5.addWidget(self.btn_target_summary)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.btn_correlation_analysis = QtWidgets.QPushButton(self.groupBox)
        self.btn_correlation_analysis.setObjectName("btn_correlation_analysis")
        self.verticalLayout_6.addWidget(self.btn_correlation_analysis)
        self.btn_refresh_table = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_refresh_table.setFont(font)
        self.btn_refresh_table.setObjectName("btn_refresh_table")
        self.verticalLayout_6.addWidget(self.btn_refresh_table)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(312, 12, 771, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.table_data = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(0)
        self.table_data.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.table_data)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_data_name, self.btn_load_data)
        MainWindow.setTabOrder(self.btn_load_data, self.txt_head_number)
        MainWindow.setTabOrder(self.txt_head_number, self.btn_tail)
        MainWindow.setTabOrder(self.btn_tail, self.btn_shape)
        MainWindow.setTabOrder(self.btn_shape, self.btn_data_types)
        MainWindow.setTabOrder(self.btn_data_types, self.btn_none_values)
        MainWindow.setTabOrder(self.btn_none_values, self.btn_data_describe)
        MainWindow.setTabOrder(self.btn_data_describe, self.btn_data_information)
        MainWindow.setTabOrder(self.btn_data_information, self.txt_summary_name)
        MainWindow.setTabOrder(self.txt_summary_name, self.ckBox_summary_plot)
        MainWindow.setTabOrder(self.ckBox_summary_plot, self.btn_num_summary)
        MainWindow.setTabOrder(self.btn_num_summary, self.txt_target_summary_name)
        MainWindow.setTabOrder(self.txt_target_summary_name, self.ckBox_plot_target)
        MainWindow.setTabOrder(self.ckBox_plot_target, self.btn_target_summary)
        MainWindow.setTabOrder(self.btn_target_summary, self.btn_correlation_analysis)
        MainWindow.setTabOrder(self.btn_correlation_analysis, self.table_data)
        MainWindow.setTabOrder(self.table_data, self.txt_shape)

        self.btn_load_data.clicked.connect(self.load_data)
        self.btn_shape.clicked.connect(self.show_shape)
        self.btn_head.clicked.connect(self.show_df_head)
        self.btn_tail.clicked.connect(self.show_df_tail)
        self.btn_data_types.clicked.connect(self.show_data_types)
        self.btn_refresh_table.clicked.connect(self.refresh_table)
        self.btn_none_values.clicked.connect(self.show_none_sums)
        self.btn_data_describe.clicked.connect(self.data_describe)
        self.btn_data_information.clicked.connect(self.show_data_info)
        self.btn_num_summary.clicked.connect(self.column_summary)
        self.btn_target_summary.clicked.connect(self.target_summary)
        self.btn_correlation_analysis.clicked.connect(self.correlation_analysis)
        self.btn_FillNoneValues.clicked.connect(self.fill_NA_Values)
        self.btn_Encode.clicked.connect(self.encode_df)
        self.btn_RFModel.clicked.connect(self.RF_Model)
        self.btn_Predict.clicked.connect(self.Predict)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualizer Program"))
        self.label.setText(_translate("MainWindow", "Data Name:"))
        self.txt_data_name.setPlaceholderText(_translate("MainWindow", "Dataset"))
        self.txt_head_number.setToolTip(_translate("MainWindow", "Numeric value of for your choice of first or last of dataset"))
        self.txt_head_number.setPlaceholderText(_translate("MainWindow", "5"))
        self.btn_tail.setToolTip(_translate("MainWindow", "Shows the last rows of the dataset for desired number"))
        self.btn_tail.setText(_translate("MainWindow", "Tail"))
        self.btn_head.setToolTip(_translate("MainWindow", "Shows the first rows of dataset for desired number"))
        self.btn_head.setText(_translate("MainWindow", "Head"))
        self.btn_shape.setToolTip(_translate("MainWindow", "Shows the row and column number"))
        self.btn_shape.setText(_translate("MainWindow", "Shape"))
        self.btn_data_types.setToolTip(_translate("MainWindow", "Shows the data types of columns in dataset"))
        self.btn_data_types.setText(_translate("MainWindow", "Data Types"))
        self.btn_none_values.setToolTip(_translate("MainWindow", "Shows the sum of none values for each column in dataset"))
        self.btn_none_values.setText(_translate("MainWindow", "None Values"))
        self.btn_data_information.setToolTip(_translate("MainWindow", "Shows the information for each column"))
        self.btn_data_information.setText(_translate("MainWindow", "Data Information"))
        self.btn_data_describe.setToolTip(_translate("MainWindow", "Shows the statistical values of columns"))
        self.btn_data_describe.setText(_translate("MainWindow", "Data Describe"))
        self.btn_load_data.setToolTip(_translate("MainWindow", "Loads the example dataset from the seaborn library"))
        self.btn_load_data.setText(_translate("MainWindow", "Load Data"))
        self.chkBox_data.setText(_translate("MainWindow", "Chose File"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Create Machine Learning Model"))
        self.btn_FillNoneValues.setText(_translate("MainWindow", "Fill NA Values"))
        self.btn_Encode.setText(_translate("MainWindow", "Encode"))
        self.txt_TargetName.setPlaceholderText(_translate("MainWindow", "Target Name"))
        self.btn_RFModel.setText(_translate("MainWindow", "RF Model"))
        self.chk_SaveModel.setText(_translate("MainWindow", "Save Model"))
        self.btn_Predict.setText(_translate("MainWindow", "Predict"))
        self.ckBox_summary_plot.setText(_translate("MainWindow", "Plot"))
        self.txt_summary_name.setToolTip(_translate("MainWindow", "To see all categorical or numerical column summaries, dont click plot. To see the plot for specific column summary click plot"))
        self.txt_summary_name.setPlaceholderText(_translate("MainWindow", "Column Name"))
        self.btn_num_summary.setToolTip(_translate("MainWindow", "Shows the column summary"))
        self.btn_num_summary.setText(_translate("MainWindow", "Column Summary"))
        self.ckBox_plot_target.setText(_translate("MainWindow", "Plot"))
        self.txt_target_summary_name.setToolTip(_translate("MainWindow", "Targeted column for target analysis"))
        self.txt_target_summary_name.setPlaceholderText(_translate("MainWindow", "Targeted Column"))
        self.txt_target.setToolTip(_translate("MainWindow", "Actual target in dataset"))
        self.txt_target.setPlaceholderText(_translate("MainWindow", "Target"))
        self.btn_target_summary.setToolTip(_translate("MainWindow", "Shows the target analysis"))
        self.btn_target_summary.setText(_translate("MainWindow", "Target Summary"))
        self.btn_correlation_analysis.setToolTip(_translate("MainWindow", "Shows the correlation analysis of dataset"))
        self.btn_correlation_analysis.setText(_translate("MainWindow", "Correlation Analysis"))
        self.btn_refresh_table.setToolTip(_translate("MainWindow", "Refresh the table to beginning"))
        self.btn_refresh_table.setText(_translate("MainWindow", "Refresh Table"))

    def load_data(self):
        """
        Load data from a dataset specified by the user input and populate a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset using
        the Seaborn library, display the data in a table widget, and handle any potential errors.

        Returns:
            DataFrame or None: Loaded DataFrame if successful, None otherwise.
        """
        try:
            if self.dataFrame is not None:
                # If data is already loaded, return it directly
                return self.dataFrame

            if not self.chkBox_data.isChecked():
                data_name = self.txt_data_name.text().strip()
                
                if data_name == "":
                    QMessageBox.warning(None, "Error", "Please enter a dataset name.")
                    return None
                
                # Load the dataset using Seaborn and convert it to a pandas DataFrame
                data = sns.load_dataset(data_name)
                self.dataFrame = pd.DataFrame(data)
            else:
                dataset_path, _ = QFileDialog.getOpenFileName(None, "Select Dataset File", "", "CSV Files (*.csv);;All Files (*)")
                if not dataset_path:
                    QMessageBox.warning(None, "Error", "No file selected.")
                    return None

                self.dataFrame = pd.read_csv(dataset_path)
                
            # Disable the text input field to prevent further changes
            self.txt_data_name.setEnabled(False)

            # Get the dimensions of the DataFrame
            num_rows, num_cols = self.dataFrame.shape

            # Clear any existing content in the table widget
            self.table_data.clear()

            # Set the number of rows and columns in the table widget
            self.table_data.setRowCount(num_rows)
            self.table_data.setColumnCount(num_cols)

            # Set column names based on the DataFrame's columns
            column_names = list(self.dataFrame.columns)
            self.table_data.setHorizontalHeaderLabels(column_names)

            # Populate the table widget with data from the DataFrame
            for i in range(num_rows):
                for j in range(num_cols):
                    item = QTableWidgetItem(str(self.dataFrame.iat[i, j]))
                    self.table_data.setItem(i, j, item)

            return self.dataFrame

        except Exception as e:
            # If an error occurs, display a warning message with details of the error
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")
            return None

    def show_shape(self):
        """
        Display the shape (number of rows and columns) of the loaded dataset.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, calculate the number of rows and columns in the dataset,
        and display the shape in a text field.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or shape calculation,
                                a warning message dialog is displayed to the user with details
                                of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Calculate the number of rows and columns in the DataFrame
                num_rows, num_cols = dataFrame.shape

                # Create a string representation of the shape (number of rows and columns)
                shape = f"{num_rows} - {num_cols}"

                # Set the shape string in the text field and disable further editing
                self.txt_shape.setText(shape)
                self.txt_shape.setEnabled(False)
        
        except Exception as e:
            # If an error occurs, display a warning message with details of the error
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def show_df_head(self):
        """
        Display the first few rows of the loaded dataset in a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, retrieve the specified number of rows to display,
        and populate a table widget with the selected rows of the DataFrame.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:

                if self.txt_head_number.text() == "":
                    QMessageBox.warning(None, "Error", f"Please type a head number.")
                
                else:
                    # Retrieve the specified number of rows to display
                    head = int(self.txt_head_number.text())

                    # Get the first few rows of the DataFrame
                    head_dataFrame = dataFrame.head(head)

                    # Get the dimensions of the DataFrame
                    num_rows, num_cols = head_dataFrame.shape

                    # Set the number of rows and columns in the table widget
                    self.table_data.setRowCount(num_rows)
                    self.table_data.setColumnCount(num_cols)

                    # Set column names in the table widget
                    column_names = list(head_dataFrame.columns)
                    self.table_data.setHorizontalHeaderLabels(column_names)

                    # Populate the table widget with data from the DataFrame
                    for i in range(num_rows):
                        for j in range(num_cols):
                            item = QTableWidgetItem(str(head_dataFrame.iat[i, j]))
                            self.table_data.setItem(i, j, item)
            
        except ValueError as ve:
            # Handle ValueError (e.g., invalid input for row count)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")
        
        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")
        
        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def show_df_tail(self):
        """
        Display the last few rows of the loaded dataset in a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, retrieve the specified number of rows from the end,
        and populate a table widget with the selected rows of the DataFrame.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:

                if self.txt_head_number.text() == "":
                    QMessageBox.warning(None, "Error", f"Please type a tail number.")
                else:
                    # Retrieve the specified number of rows from the end to display
                    tail = int(self.txt_head_number.text())

                    # Get the last few rows of the DataFrame
                    tail_dataFrame = dataFrame.tail(tail)

                    # Get the dimensions of the DataFrame
                    num_rows, num_cols = tail_dataFrame.shape

                    # Set the number of rows and columns in the table widget
                    self.table_data.setRowCount(num_rows)
                    self.table_data.setColumnCount(num_cols)

                    # Set column names in the table widget
                    column_names = list(tail_dataFrame.columns)
                    self.table_data.setHorizontalHeaderLabels(column_names)

                    # Populate the table widget with data from the DataFrame
                    for i in range(num_rows):
                        for j in range(num_cols):
                            item = QTableWidgetItem(str(tail_dataFrame.iat[i, j]))
                            self.table_data.setItem(i, j, item)
            
        
        except ValueError as ve:
            # Handle ValueError (e.g., invalid input for row count)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")
        
        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")
        
        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def show_data_types(self):
        """
        Display the data types of columns in the loaded dataset in a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, retrieve the data types of columns, and display them
        in a table widget.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """

        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Get the column names from the DataFrame
                column_names = list(dataFrame.columns)

                # Clear existing content and set column names in the table widget
                self.table_data.clear()
                self.table_data.setColumnCount(len(column_names))
                self.table_data.setHorizontalHeaderLabels(column_names)

                # Retrieve the data types of columns from the DataFrame
                dataTypes = dataFrame.dtypes

                # Display data types in the first row of the table widget
                for i, column_name in enumerate(column_names):
                    item = QTableWidgetItem(str(dataTypes[column_name]))
                    self.table_data.setItem(0, i, item)

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def refresh_table(self):
        """
        Refresh the table widget with the latest data from the dataset.

        This method interacts with a graphical user interface (GUI) to reload the dataset
        and update the table widget with the latest data. It also enables the data name
        input field for further changes.

        Returns:
            None
        """

        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Get the dimensions of the DataFrame
                num_rows, num_cols = dataFrame.shape

                # Clear any existing content in the table widget
                self.table_data.clear()

                # Set the number of rows and columns in the table widget
                self.table_data.setRowCount(num_rows)
                self.table_data.setColumnCount(num_cols)

                # Set column names based on the DataFrame's columns
                column_names = list(dataFrame.columns)
                self.table_data.setHorizontalHeaderLabels(column_names)

                # Populate the table widget with data from the DataFrame
                for i in range(num_rows):
                    for j in range(num_cols):
                        item = QTableWidgetItem(str(dataFrame.iat[i, j]))
                        self.table_data.setItem(i, j, item)

                # Enable the data name input field
                self.txt_data_name.setEnabled(True)

        except Exception as e:
            # Handle any unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def show_none_sums(self):
        """
        Display the number of null values in each column of the loaded dataset in a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, count the number of null values in each column,
        and display the counts in a table widget.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Get the column names from the DataFrame
                column_names = list(dataFrame.columns)

                # Clear existing content and set column names in the table widget
                self.table_data.clear()
                self.table_data.setColumnCount(len(column_names))
                self.table_data.setHorizontalHeaderLabels(column_names)

                # Count the number of null values in each column and display in the first row
                for i, column_name in enumerate(column_names):
                    num_nulls = dataFrame[column_name].isnull().sum()
                    item = QTableWidgetItem(str(num_nulls))
                    self.table_data.setItem(0, i, item)

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def data_describe(self):
        """
        Display descriptive statistics of the loaded dataset in a QTableWidget.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, compute descriptive statistics, and display them
        in a table widget.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Clear existing content in the table widget
                self.table_data.clear()

                # Compute descriptive statistics and transpose the result for easier display
                described_data = dataFrame.describe().T

                # Set the number of rows and columns in the table widget
                self.table_data.setRowCount(len(described_data))
                self.table_data.setColumnCount(len(described_data.columns))

                # Set column names in the table widget
                column_names = described_data.columns
                self.table_data.setHorizontalHeaderLabels(column_names)

                # Set index names in the table widget
                index_names = described_data.index.tolist()
                self.table_data.setVerticalHeaderLabels(index_names)

                # Populate the table widget with the described data
                for i, (_, row) in enumerate(described_data.iterrows()):
                    for j, value in enumerate(row):
                        # Format value to have only two digits after the decimal point
                        formatted_value = "{:.2f}".format(value)
                        item = QTableWidgetItem(formatted_value)
                        self.table_data.setItem(i, j, item)

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def show_data_info(self):
        """
        Display information about each column in the loaded dataset in a QMessageBox.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, gather information about each column (such as data type,
        non-null count, and total count), and display the information in a message box.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Create a message box
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Data Information")

                # Add a label for each column's information
                for column_name in dataFrame.columns:
                    # Gather column information
                    data_type = str(dataFrame[column_name].dtype)
                    non_null_count = dataFrame[column_name].notnull().sum()
                    total_count = len(dataFrame[column_name])

                    # Construct information text
                    info_text = (f"Column Name: {column_name}\n"
                                f"Data Type: {data_type}\n"
                                f"Non-null Count: {non_null_count}/{total_count}\n"
                                f"----------------------------------------------\n")

                    # Create a label with the information text
                    info_label = QLabel(info_text)
                    info_label.setMinimumSize(300, 100)

                    # Add the label to the message box layout
                    msg_box.layout().addWidget(info_label)

                # Set the message box to be modal
                msg_box.setModal(True)

                # Show the message box
                msg_box.exec_()

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def grab_col_names(self, dataframe, cat_th=10, car_th=20):
        """
        Identify and categorize column names based on their data types and cardinality.

        This method takes a DataFrame as input and categorizes its columns into four groups:
        categorical columns, numeric columns, categorical columns with high cardinality,
        and numeric columns treated as categorical based on a threshold.

        Args:
            dataframe (pd.DataFrame): The DataFrame to analyze.
            cat_th (int): Threshold for considering numeric columns as categorical.
                        Default is 10.
            car_th (int): Threshold for considering categorical columns as high cardinality.
                        Default is 20.

        Returns:
            tuple: A tuple containing four lists:
                1. Categorical columns
                2. Numeric columns
                3. Categorical columns with high cardinality
                4. Numeric columns treated as categorical

        Raises:
            QMessageBox.warning: If an error occurs during column categorization,
                                a warning message dialog is displayed with details of the error.
        """
        try:
            # Categorical columns
            cat_cols = [col for col in dataframe.columns if dataframe[col].dtype in ['category', 'object', 'bool']]

            # Numeric but treated as categorical
            num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th 
                        and dataframe[col].dtype in ['uint8', 'int64', 'float64']]

            # Categorical but cardinal
            cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th 
                        and dataframe[col].dtype in ['category', 'object']]

            cat_cols += num_but_cat

            # Remove overlapping columns
            cat_cols = [col for col in cat_cols if col not in cat_but_car]

            # Numeric columns
            num_cols = [col for col in dataframe.columns if col not in cat_cols]

            return cat_cols, num_cols, cat_but_car, num_but_cat

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def column_summary(self):
        """
        Generate summaries for categorical and numerical columns in the dataset.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, categorize columns, and provide summaries based on user input.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """

        try:
            # Load the dataset
            dataFrame = self.load_data()

            if dataFrame is not None:
                # Get categorical and numerical columns
                cat_cols, num_cols, _, _ = self.grab_col_names(dataFrame)
                col_name = self.txt_summary_name.text()

                # Check if the specified column name is in categorical columns
                if col_name in cat_cols:
                    # Generate summary for categorical column
                    if self.ckBox_summary_plot.isChecked():
                        # Show count plot with percentages
                        ax = sns.countplot(x=col_name, data=dataFrame)
                        for p in ax.patches:
                            height = p.get_height()
                            ratio = height / len(dataFrame) * 100
                            ax.annotate(f'{height} ({ratio:.2f}%)', (p.get_x() + p.get_width() / 2., height),
                                        ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                                        textcoords='offset points')
                        plt.show(block=True)
                    else:
                        # Display categorical data information in a message box
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Categorical Data Information")
                        layout = msg_box.layout()
                        for column_name in cat_cols:
                            ratios = 100 * dataFrame[column_name].value_counts() / len(dataFrame)
                            info_text = (
                                f"---------------------------------------------------------\n"
                                f"Ratio of {column_name}:\n{ratios}\n"
                                f"---------------------------------------------------------\n"
                            )
                            info_label = QLabel(info_text)
                            info_label.setMinimumSize(300, 100)
                            layout.addWidget(info_label)
                        msg_box.setModal(True)
                        msg_box.exec_()

                # Check if the specified column name is in numerical columns
                elif col_name in num_cols:
                    # Generate summary for numerical column
                    if self.ckBox_summary_plot.isChecked():
                        # Show histogram with KDE
                        sns.histplot(x=col_name, data=dataFrame, kde=True)
                        plt.show(block=True)
                    else:
                        # Display numerical data information in a message box
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Numerical Data Information")
                        layout = msg_box.layout()
                        for column_name in num_cols:
                            ratios = 100 * dataFrame[column_name].value_counts() / len(dataFrame)
                            info_text = (
                                f"---------------------------------------------------------\n"
                                f"Ratio of {column_name}:\n{ratios}\n"
                                f"---------------------------------------------------------\n"
                            )
                            info_label = QLabel(info_text)
                            info_label.setMinimumSize(300, 100)
                            layout.addWidget(info_label)
                        msg_box.setModal(True)
                        msg_box.exec_()

                else:
                    # Display a message for invalid column name
                    print("Invalid input: column name not found in categorical or numerical columns")

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def target_summary(self):
        """
        Generate summary statistics of the target variable grouped by another column.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, extract categorical and numerical columns, and generate
        summary statistics of the target variable grouped by a specified column.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """

        try:
            # Load the dataset if not already loaded
            if not hasattr(self, 'dataFrame') or self.dataFrame is None:
                self.dataFrame = self.load_data()

            if self.dataFrame is not None:
                # Get categorical and numerical columns
                cat_cols, num_cols, _, _ = self.grab_col_names(self.dataFrame)

                # Retrieve target variable and column name for summary
                target = self.txt_target.text()
                summary_name = self.txt_target_summary_name.text()

                # Check if the summary column exists in categorical or numerical columns
                if summary_name in cat_cols:
                    # Summary with categorical data
                    targeted_data = pd.DataFrame({"Target Mean": self.dataFrame.groupby(summary_name)[target].mean()})
                    
                    # Display summary with a bar chart if requested
                    if self.ckBox_plot_target.isChecked():
                        plt.figure(figsize=(10, 6))
                        sns.barplot(x=targeted_data.index, y="Target Mean", data=targeted_data, palette="viridis")
                        plt.xlabel(summary_name)
                        plt.ylabel("Mean of Target")
                        plt.title(f'Mean of {target} by {summary_name}')
                        plt.xticks(rotation=45, ha='right')
                        plt.tight_layout()
                        plt.show()
                    else:
                        # Display summary in a message box
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Target Summary with Categorical Data")
                        layout = msg_box.layout()
                        for category, mean in targeted_data.iterrows():
                            info_text = (
                                f"----------------------------------------\n"
                                f"{summary_name}: {category}\nTarget Mean: {mean['Target Mean']}\n"
                                f"----------------------------------------\n")
                            info_label = QLabel(info_text)
                            info_label.setMinimumSize(300, 100)
                            layout.addWidget(info_label)
                        msg_box.setModal(True)
                        msg_box.exec_()

                elif summary_name in num_cols:
                    # Summary with numerical data
                    targeted_data = pd.DataFrame({"Target Mean": self.dataFrame.groupby(summary_name)[target].mean()})
                    
                    # Display summary with a box plot if requested
                    if self.ckBox_plot_target.isChecked():
                        plt.figure(figsize=(10, 6))
                        sns.boxplot(x=target, y=summary_name, data=self.dataFrame, palette="viridis")
                        plt.xlabel(target)
                        plt.ylabel(summary_name)
                        plt.title(f'{summary_name} by {target}')
                        plt.xticks(rotation=45, ha='right')
                        plt.tight_layout()
                        plt.show()
                    else:
                        # Display summary in a message box
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Target Summary with Numerical Data")
                        layout = msg_box.layout()
                        for category, mean in targeted_data.iterrows():
                            info_text = (
                                f"{target}: {category}\nTarget Mean: {mean['Target Mean']}\n"
                                f"--------------------------\n")
                            info_label = QLabel(info_text)
                            info_label.setMinimumSize(300, 100)
                            layout.addWidget(info_label)
                        msg_box.setModal(True)
                        msg_box.exec_()

                else:
                    # Display a warning if the target column is not found in the dataset
                    QMessageBox.warning(None, "Warning", "Target columns cannot be found in the dataset. Please make sure you typed it correctly.")

        except ValueError as ve:
            # Handle ValueError (e.g., invalid input or operation)
            QMessageBox.warning(None, "Value Error", f"An error occurred: {ve}")

        except TypeError as te:
            # Handle TypeError (e.g., invalid type conversion)
            QMessageBox.warning(None, "Type Error", f"An error occurred: {te}")

        except Exception as e:
            # Handle any other unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def correlation_analysis(self, corr_th=0.90):
        """
        Perform correlation analysis on numerical columns of the dataset and visualize the correlation matrix.

        This method interacts with a graphical user interface (GUI) to load a dataset
        using the Seaborn library, identify numerical columns, compute the correlation matrix,
        and visualize it as a heatmap.

        Args:
            corr_th (float): Threshold for considering strong correlation.
                            Default is 0.90.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during data loading or display,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """

        try:
            # Load the dataset if not already loaded
            if not hasattr(self, 'dataFrame') or self.dataFrame is None:
                self.dataFrame = self.load_data()

            if self.dataFrame is not None:
                # Select numerical columns
                num_cols = [col for col in self.dataFrame.columns if self.dataFrame[col].dtypes in ["uint8", "int64", "float64"]]

                # Compute correlation matrix
                corr = self.dataFrame[num_cols].corr()
                corr_matrix = corr.abs()

                # Visualize correlation matrix as a heatmap
                sns.set(rc={'figure.figsize': (6, 3)})
                sns.heatmap(corr_matrix, cmap="RdBu", annot=True)

                plt.show()

        except Exception as e:
            # Handle any unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def fill_NA_Values(self):
        """
        Fill missing values in the DataFrame.

        This method fills missing values in numerical columns with their median,
        and leaves categorical columns unchanged.

        Args:
            dataframe (pd.DataFrame): The DataFrame to fill missing values.

        Returns:
            pd.DataFrame: The DataFrame with missing values filled.

        Raises:
            QMessageBox.warning: If an error occurs during data processing,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            # Fill missing values in numerical columns with median
            self.dataFrame = self.dataFrame.apply(lambda x: x.fillna(x.median()) if x.dtype not in ["category", "object", "bool"] else x, axis=0)
            try:
                if self.dataFrame is not None:
                    # Get the dimensions of the DataFrame
                    num_rows, num_cols = self.dataFrame.shape

                    # Clear any existing content in the table widget
                    self.table_data.clear()

                    # Set the number of rows and columns in the table widget
                    self.table_data.setRowCount(num_rows)
                    self.table_data.setColumnCount(num_cols)

                    # Set column names based on the DataFrame's columns
                    column_names = list(self.dataFrame.columns)
                    self.table_data.setHorizontalHeaderLabels(column_names)

                    # Populate the table widget with data from the DataFrame
                    for i in range(num_rows):
                        for j in range(num_cols):
                            item = QTableWidgetItem(str(self.dataFrame.iat[i, j]))
                            self.table_data.setItem(i, j, item)

                return self.dataFrame

            except Exception as e:
                # Handle any unexpected exceptions
                QMessageBox.warning(None, "Error", f"An error occurred: {e}")

        except Exception as e:
            # Handle any unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def encode_df(self, drop_first=True):
        """
        Encode categorical columns in the DataFrame.

        This method one-hot encodes categorical columns in the DataFrame.

        Args:
            dataframe (pd.DataFrame): The DataFrame to encode.
            drop_first (bool): Whether to drop the first encoded column for each categorical feature.
                            Default is True.

        Returns:
            pd.DataFrame: The DataFrame with categorical columns encoded.

        Raises:
            QMessageBox.warning: If an error occurs during data processing,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            # Get column names
            cat_cols, _, _, _ = self.grab_col_names(self.dataFrame)
            
            # One-hot encode categorical columns
            self.dataFrame = pd.get_dummies(self.dataFrame, columns=cat_cols, drop_first=drop_first)

            if self.dataFrame is not None:
                    # Get the dimensions of the DataFrame
                    num_rows, num_cols = self.dataFrame.shape

                    # Clear any existing content in the table widget
                    self.table_data.clear()

                    # Set the number of rows and columns in the table widget
                    self.table_data.setRowCount(num_rows)
                    self.table_data.setColumnCount(num_cols)

                    # Set column names based on the DataFrame's columns
                    column_names = list(self.dataFrame.columns)
                    self.table_data.setHorizontalHeaderLabels(column_names)

                    # Populate the table widget with data from the DataFrame
                    for i in range(num_rows):
                        for j in range(num_cols):
                            item = QTableWidgetItem(str(self.dataFrame.iat[i, j]))
                            self.table_data.setItem(i, j, item)
                            
            return self.dataFrame
        except Exception as e:
            # Handle any unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")
    
    def RF_Model(self):
        """
        Train and evaluate a Random Forest model on the given DataFrame.

        This method trains a Random Forest model, optionally displays results in a message box,
        plots feature importance, and saves the model to a file.

        Args:
            dataframe (pd.DataFrame): The DataFrame containing the data.
            target (str): The target variable name.
            test_size (float): Proportion of the dataset to include in the test split. Default is 0.20.
            cv (int): Number of cross-validation folds. Default is 10.
            results (bool): Whether to display evaluation results in a message box. Default is False.
            plot_importance (bool): Whether to plot feature importance. Default is False.
            save_results (bool): Whether to save the trained model to a file. Default is False.

        Returns:
            None

        Raises:
            QMessageBox.warning: If an error occurs during model training or evaluation,
                                a warning message dialog is displayed to the user with
                                details of the error.
        """
        try:
            target = self.txt_TargetName.text()
            
            # Split the data into training and testing sets
            X = self.dataFrame.drop(target, axis=1)
            y = self.dataFrame[target]
            test_size = 0.20  # Set test_size here
            cv=10
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=1)
            
            # Train the Random Forest model
            rf_model = RandomForestRegressor(random_state=1).fit(X_train, y_train)
            

            feature_imp = pd.DataFrame({'Value': rf_model.feature_importances_, 'Feature': X.columns})
            plt.figure(figsize=(8, 6))
            sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value", ascending=False))
            plt.title("Feature Importance")
            plt.tight_layout()
            plt.savefig("importance.jpg")
            plt.show()              

            # Calculate evaluation metrics
            mse_train = mean_squared_error(y_train, rf_model.predict(X_train))
            mse_test = mean_squared_error(y_test, rf_model.predict(X_test))
            rmse_train = np.sqrt(mse_train)
            rmse_test = np.sqrt(mse_test)
            mae_train = mean_absolute_error(y_train, rf_model.predict(X_train))
            mae_test = mean_absolute_error(y_test, rf_model.predict(X_test))
            r2_train = rf_model.score(X_train, y_train)
            r2_test = rf_model.score(X_test, y_test)
            cv_results_mse = cross_validate(rf_model, X, y, cv=cv, scoring="neg_mean_squared_error")
            cv_results_rmse = cross_validate(rf_model, X, y, cv=cv, scoring="neg_root_mean_squared_error")

            # Prepare results text
            results_text = (f"MSE Train: {mse_train:.3f}\n"
                            f"MSE Test: {mse_test:.3f}\n"
                            f"RMSE Train: {rmse_train:.3f}\n"
                            f"RMSE Test: {rmse_test:.3f}\n"
                            f"MAE Train: {mae_train:.3f}\n"
                            f"MAE Test: {mae_test:.3f}\n"
                            f"R2 Train: {r2_train:.3f}\n"
                            f"R2 Test: {r2_test:.3f}\n"
                            f"Cross Validate MSE: {-cv_results_mse['test_score'].mean():.3f}\n"
                            f"Cross Validate RMSE: {-cv_results_rmse['test_score'].mean():.3f}\n")

            # Display results in a message box
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Random Forest Model Results")
            msg_box.setText(results_text)
            msg_box.setModal(True)
            msg_box.exec_()

            if self.chk_SaveModel.isChecked():
                # Save the trained model to a file
                joblib.dump(rf_model, "rf_model.pkl")
        
        except Exception as e:
            # Handle any unexpected exceptions
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    def load_model(self):
        """
        Load the trained Random Forest model from a file.

        Returns:
            model_disc (RandomForestRegressor): The loaded Random Forest model.
        """
        try:
            model_disc = joblib.load("rf_model.pkl")
            return model_disc
        except Exception as e:
            QMessageBox.warning(None, "Error", f"An error occurred while loading the model: {e}")
            return None

    def Predict(self):
        """
        Predict using the loaded model and a random sample from the data.

        Returns:
            predictions (np.array): The predicted values.
        """
        try:
            target = self.txt_TargetName.text()
            X = self.dataFrame.drop(target, axis=1)
            random_baseballer = X.sample(1).values.tolist()[0]      
            model_disc = self.load_model()
            if model_disc is None:
                raise ValueError("Model could not be loaded.")

            # Making prediction
            random_baseballer_df = pd.DataFrame([random_baseballer], columns=X.columns)
            predictions = model_disc.predict(random_baseballer_df)

            # Prepare the input data and prediction results text
            input_data_text = "\n".join([f"{col}: {val}" for col, val in zip(X.columns, random_baseballer)])
            prediction_text = f"Prediction: {predictions[0]:.3f}"

            # Display the input data and predictions in a message box
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Prediction Results")
            msg_box.setText(f"Input Data:\n{input_data_text}\n\n{prediction_text}")
            msg_box.setModal(True)
            msg_box.exec_()

            return predictions
        except Exception as e:
            QMessageBox.warning(None, "Error", f"An error occurred during prediction: {e}")
            return None

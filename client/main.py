import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem





# 生成示例 K 线数据
data = {
    'Open':   [20, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24, 22, 21, 23, 24],
    'High':   [25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25, 24, 23, 26, 25],
    'Low':    [19, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23, 20, 20, 22, 23],
    'Close':  [23, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24],
    'Volume': [23, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24, 21, 22, 25, 24]
}
df = pd.DataFrame(data)


class KLineTableApp(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主布局
        layout = QVBoxLayout()

        # 创建 K 线图
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # 绘制 K 线图
        ax = self.figure.add_subplot(111)
        ax.plot(df['Open'], label='Open')
        ax.plot(df['High'], label='High')
        ax.plot(df['Low'], label='Low')
        ax.plot(df['Close'], label='Close')
        ax.legend()

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        # 填充表格数据
        for row in range(len(df)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table.setItem(row, col, item)

        # 将 K 线图和表格添加到布局中
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.table)

        # 设置布局
        self.setLayout(layout)
        self.setWindowTitle('K 线图与表格示例')
        self.setGeometry(100, 100, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KLineTableApp()
    window.show()
    sys.exit(app.exec_())

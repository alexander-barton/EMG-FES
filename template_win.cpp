#include "template_win.h"
#include "ui_template_win.h"
#include <QTimeLine>
#include <QDebug>
#include <QMessageBox>

Template_win::Template_win(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Template_win)
{
    ui->setupUi(this);
    // Construct a 10-second timeline (10,000ms) with a frame range of 0 - 100
    QTimeLine *timeLine = new QTimeLine(10000, this);
    timeLine->setFrameRange(0, 100);
    timeLine->start();
    connect(timeLine, SIGNAL(frameChanged(int)), ui->progressBar, SLOT(setValue(int)));
}

Template_win::~Template_win()
{
    delete ui;
}

void Template_win::on_progressBar_valueChanged(int value)
{
    if (value == 100)
    {
        qDebug() << "Calibration complete!";
        close();
        QMessageBox msgBox;
        msgBox.setText("Calibration completed!");
        msgBox.exec();
    }
}

#include "adjuster.h"
#include "ui_adjuster.h"
#include <QDebug>

Adjuster::Adjuster(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Adjuster)
{
    ui->setupUi(this);
}

Adjuster::~Adjuster()
{
    delete ui;
}

void Adjuster::on_verticalSlider_valueChanged(int value)
{
    qDebug() << "Sensitivity value:";
    qDebug() << value;
}

#include "primaryui.h"
#include "ui_primaryui.h"
#include <QMessageBox>
#include "adjuster.h"
#include <QDebug>

PrimaryUI::PrimaryUI(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::PrimaryUI)
{
    ui->setupUi(this);
}

PrimaryUI::~PrimaryUI()
{
    delete ui;
}

void PrimaryUI::on_Template_clicked()
{
    //QMessageBox::question(this,tr("Warning!"),tr("Are you sure?"));
    QMessageBox::StandardButton reply;
    reply = QMessageBox::question(this, "test", "Are you sure?", QMessageBox::Yes|QMessageBox::No);

    if (reply == QMessageBox::Yes)
    {
        qDebug() << "yes was clicked";
        //hide();
        Template_win = new class Template_win(this);
        Template_win->show();
    }
    else
    {
      qDebug() << "yes was *not* clicked";
}
}

void PrimaryUI::on_Training_clicked()
{
    hide();
    SecDialog = new class SecDialog(this);
    SecDialog->show();
}

#include "secdialog.h"
#include "ui_secdialog.h"
#include "adjuster.h"
#include <QMessageBox>
#include <QDebug>

SecDialog::SecDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SecDialog)
{
    ui->setupUi(this);
}

SecDialog::~SecDialog()
{
    delete ui;
}

void SecDialog::on_Adjust_clicked()
{
    Adjuster *adjusterbutton = new Adjuster(this);
    adjusterbutton->setModal(true);
    adjusterbutton->exec();
}

void SecDialog::on_Stop_clicked()
{
    QMessageBox::StandardButton reply;
    reply = QMessageBox::question(this, "test", "Are you sure?", QMessageBox::Yes|QMessageBox::No);

    if (reply == QMessageBox::Yes)
    {
        qDebug() << "yes was clicked";
        QApplication::quit();
    }
    else
    {
      qDebug() << "yes was *not* clicked";
}
}

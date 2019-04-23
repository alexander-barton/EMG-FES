#include "primaryui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    PrimaryUI w;
    w.show();

    return a.exec();
}

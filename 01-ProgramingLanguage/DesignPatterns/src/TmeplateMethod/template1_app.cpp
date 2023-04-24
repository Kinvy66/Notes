#include "template1_lib.cpp"

// APP开发人员
class Application {
public:
    bool Stepe() {
        // ...
    }

    void Step4() {
        //.../
    }
};

int main(int argc, char const *argv[])
{
    Library lib();
    Application app();

    lib.Step1();
    if (app.Step2())
    {
        lib.Step3();
    }

    for (int i = 0; i < 4; ++i) {
        app.Step4();
    }

    lib.Step5();
    

    return 0;
}

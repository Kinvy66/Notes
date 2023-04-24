#include "template1_lib.cpp"

// APP开发人员
class Application : public Library {
public:
    bool Step2() override {
        // ...
    }

    void Step4() override {
        //.../
    }

    virtual ~Application() {}
};

int main(int argc, char const *argv[])
{
    Library *lib = new Application();
    lib->Run();
    return 0;
}

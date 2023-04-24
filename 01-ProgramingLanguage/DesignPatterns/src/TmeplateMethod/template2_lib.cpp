// Lib 开发人员

class Library{
protected :
    void Step1() { }
    void Step3() { }
    void Stped5() { }
    virtual bool Step2() {}
    virtual void Step4();

public:
    void Run() {
        Step1();
        if (Step2())
        {
            Step3();
        }

        for (int i = 0; i < 4; ++i)
        {
            Step4();
        }
        Step5();
    }
    virtual ~Library()
};
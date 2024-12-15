package src.LR.LR5_8_test;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

class TelevisionSchedule {
    private List<TelevisionProgram> programs;

    public TelevisionSchedule() {
        programs = new ArrayList<>();
    }
    
    public void addProgram(TelevisionProgram program) {
        programs.add(program);
    }
    
    public List<TelevisionProgram> getPrograms() {
        return programs;
    }
}

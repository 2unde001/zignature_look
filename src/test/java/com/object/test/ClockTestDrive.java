package com.object.test;

import com.object.ClockTime;
import org.junit.Test;

public class ClockTestDrive
{
    @Test
    public void validateRealTime(){
        ClockTime c = new ClockTime();

        c.setTime("12");

        String tod = c.getTime();

        System.out.println("time:" + tod);
    }
}

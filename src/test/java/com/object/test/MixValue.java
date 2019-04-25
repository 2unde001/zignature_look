package com.object.test;

import org.junit.Test;

public class MixValue
{
    int counter = 0;
    @Test
    public void validateOutput()
    {
        int count = 0;

        MixValue[] mixValues = new MixValue[20];

        int x = 0;

        while (x < 19)
        {
             mixValues[x] = new MixValue();
             mixValues[x].counter = mixValues[x].counter + 1;
             count = count + 1;
             count = count + mixValues[x].newValue(x);
             x = x +1;
        }

        System.out.println(count + " " + mixValues[1].counter);
    }

    private int newValue(int value)
    {
        if (value < 1){
            MixValue mValue = new MixValue();
            mValue.counter = mValue.counter + 1;
            return 1;
        }
        return 0;
    }
}



package com.object.test;

import org.junit.Test;

public class ArrayTestDrive
{
    @Test
    public void validateIslandArray() {

        int [] index = new int[4];
        index[0] = 1;
        index[1] = 3;
        index[2] = 0;
        index[3] = 2;

        String[] island = new String[4];
        island[0] = "Bermuda";
        island[1] = "Fiji";
        island[2] = "Azores";
        island[3] = "Cozumel";

        int y = 0;

        int ref;

        while (y < 4)
        {
            ref = index[y];
            System.out.println("island = " + island[ref]);

            y = y + 1;

        }




    }
}

package com.object.test;

import com.object.Hobbits;
import org.junit.Test;

public class HobbitsTestDrive
{
    @Test
    public void validateName()
    {
        Hobbits[] h = new Hobbits[3];

        int x = 0;

        while (x < 3)
        {
            h[x] = new Hobbits();
            h[x].name = "Bilbo";

            if (x == 1)
            {
                h[x].name = "Frodo";
            }
            if (x == 2)
            {
                h[x].name = "Sam";
            }

            System.out.println(h[x].name + " is a ");
            System.out.println("good Hobbbit name");
            x = x + 1;
        }



    }
}

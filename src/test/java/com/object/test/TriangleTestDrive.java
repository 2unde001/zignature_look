package com.object.test;

import com.object.Triangle;
import org.junit.Test;

public class TriangleTestDrive
{


    @Test
    public void validateTriangleArea()
    {

        Triangle[] ta = new Triangle[4];

        int x = 0;

        while (x < 4)
        {
           ta[x] = new Triangle();
           ta[x].height = (x + 1) * 2;
           ta[x].length = x + 4;

           ta[x].setArea();

           System.out.print("triangle "+ x + ", area");
           System.out.println(" = " + ta[x].area);

           x = x + 1;
        }

        int y = x;
        x = 27;

        Triangle triangle = ta[2];
        ta[2].area = 343;
        System.out.print("y = " + y);
        System.out.println(", triangle area = "+ triangle.area);

    }
}

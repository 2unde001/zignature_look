package com.object.test;

import com.object.Echo;
import org.junit.Test;

public class EchoTest
{
    @Test
    public void validateEcho()
    {
        Echo echo1 = new Echo();
        Echo echo2 = echo1;


        int x = 0;

        while (x < 4)
        {
            echo1.hello();
            echo1.count = echo1.count + 1;

            if (x == 3){

                echo2.count = echo2.count + 1;
            }
            if (x > 0){
                echo2.count = echo2.count + echo1.count;
            }
            x = x + 1;

        }

        System.out.print(echo2.count);
    }
}

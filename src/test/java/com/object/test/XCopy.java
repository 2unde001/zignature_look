package com.object.test;

import org.junit.Test;

public class XCopy
{
    private int origin = 42;

    @Test
    public void validateCopyNumber()
    {
        XCopy x = new XCopy();

        int y = x.go(origin);
        System.out.println(origin + " " + y);

    }

    private int go(int arg)
    {
        arg = arg * 2;
        return arg;
    }
}

package com.object;


public class Puzzle
{
    public int x;
    public int ivar;

    public int doStuff(int factor)
    {
        if (ivar > 100){
            return ivar * factor;
        }
        else {
            return ivar * (5 - factor);
        }
    }
}

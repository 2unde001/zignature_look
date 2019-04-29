package com.object;

public class Dog
{
    public String name;
    private int x;


    public boolean bark()
    {
        System.out.println(name + " say Ruff");
        System.out.println("-----------------------------------------------------");
        return true;
    }


    public int getSize()
    {
        return x;
    }

    public int setSize(int i)
    {
        x = i;
        System.out.println("Elements available in DOg array is " + x);
        return x;
    }

}

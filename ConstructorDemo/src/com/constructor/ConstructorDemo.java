package com.constructor;


public class ConstructorDemo
{
    public class ClassConstructor
    {

        public  ClassConstructor()
        {
            System.out.println("I am the constructor");

        }

        public void getData()
        {
            System.out.println("I am the void method");
        }

    }

    public static void main(String[] args)
    {
        ClassConstructor constructor = new ClassConstructor();
        constructor.getData();
	// write your code here
    }



}



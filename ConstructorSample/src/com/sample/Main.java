package com.sample;


public class Main
{

    public static void main(String[] args)
    {
	// write your code here
        SimpleConstructor ctr1 =  new  SimpleConstructor("Hello World");

        SimpleConstructor ctr = new SimpleConstructor(2, 4);

    }

    public static class SimpleConstructor
    {
        public SimpleConstructor(String text)
        {
            System.out.println(text);
        }

        public SimpleConstructor(int a, int b)
        {
            System.out.println("I am a parameterized constructor");

            int c = a + b;
            System.out.println(c);

        }

        public void getData()
        {
            System.out.println("I am a void method");
        }


    }
}

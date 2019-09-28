package com.gameobjects;

import org.junit.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class SimpleDotComTestDrive
{


    @Test
    public void validateRandomGuessNumber()
    {
        SimpleDotCom simpleDotCom = new SimpleDotCom();

        int randomNum = (int) (Math.random() * 5);

        int[] location = {randomNum, randomNum + 1, randomNum +2};

        simpleDotCom.setLocationCell(location);

//       // check if the game is still alive
//
//        boolean isAlive = true;
//
//        while (isAlive == true){
//
//            String quess = simpleDotCom.getUserInput("Enter a number");
//
//        }

        String user = "7";
        simpleDotCom.checkYourSelf(user);
        simpleDotCom.setLocationCell(location);

    }
    @Test
    public void testeasy(){
       easy("Java is easy to lean");
        easy("if you put effort");
    }

    public void easy( String s)
    {
        System.out.println();
        System.out.println(s);
        System.out.println();
    }

    @Test
    public void main ()
    {
        int m = 5;
        int n = 6;

        System.out.println("M=" + m + " N=" + n);
        swap(m, n);
        System.out.println("M=" + m + " N=" + n);
    }

    private static void swap(int a, int b)
    {
        int c = a + b;
        a = b;
        b = c;
        System.out.println(c);
    }
//
//    @Test
//    public void mainReferenceType()
//    {
//        Student jen = new Student();
//        jen.name = "Jen";
//        jen.age = 21;
//
//        Student beth = new Student();
//        beth.name = "Beth";
//        beth.age = 15;
//
//        System.out.println("Jen is " + jen.age);
//        System.out.println("Beth is " + beth.age);
//
//        ageSwap(jen, beth);
//
//        System.out.println("Jen is " + jen.age);
//        System.out.println("Beth is " + beth.age);
//    }
//
//    private static void ageSwap(Student a,
//                                Student b)
//    {
//        int c = a.age;
//        a.age = b.age;
//        b.age = c;
//    }

    static class Student
    {
        String name;
        int age;
    }

    @Test
    public void mainPrimitive()
    {
        Student jen = new Student();
        jen.name = "Jen";
        jen.age = 21;

        Student beth = new Student();
        beth.name = "Beth";
        beth.age = 15;

        System.out.println("Jen is " + jen.age);
        System.out.println("Beth is " + beth.age);

        Student a = jen, b = beth;

        int c = a.age;
        a.age = b.age;
        b.age = c;

        System.out.println("Jen is " + jen.age);
        System.out.println("Beth is " + beth.age);
    }

    public static int min(int a, int b, int c, int d)
    {
        //write your code here
       if (min(a, b)  < min(c, d)){
           return min(a,b);
       }
       else {
            return min(c, d);
       }
    }


    @Test
    public void testLastMinValue()
    {
        System.out.println(min(-20, -10));
        System.out.println(min(-20, -10, -30, -40));
        System.out.println(min(-20, -10, -30, 40));
        System.out.println(min(-40, -10, -30, 40));
    }

    public static int min(int a, int b) {
        //write your code here

        int m;
        if(a < b){
            m = a;
        }
        else {
            m = b;
        }
        return m;
    }

    // Print Three number
    public static void print3(String s) {
        //write your code here
        for(int i = 0; i < 3 ; i++){
            System.out.println(s);
        }

    }

    @Test
    public void print3Test() {
        print3("I love you!");
    }

    // Print Three number
    public static void printWord3(String s) {
        //write your code here

        System.out.print(s +" " + s +" " + s + " " );


    }

    @Test
    public void printWord3Test() {
        printWord3("window");
        printWord3("file");
    }

    @Test
    public void concatTest() {
        Cat cat = new Cat();

        String text =  "The cat is " + cat;

        //System.out.println(text);
        System.out.println(text + cat.toString());
    }

    @Test
    public void concatInteger() {

        int a = 5;
        String s = Integer.toString(a);

        System.out.println(s);
    }

    @Test
    public void concatTwoObject() {

        int a = 5;
        Cat cat = new Cat();
        String cat1 = cat.toString();
        String cat2 = Integer.toString(a);

        System.out.println("The cat is " + cat1 + cat2);
    }

    @Test
    public void concatTwoObjectNotCompile() {

        int a = 5;
        Cat cat = new Cat();
//        String cat1 = cat.toString();
//        String cat2 = Integer.toString(a);
        String text = (((cat + Integer.toString(a)) + "The cat is ") + cat) + a;
    }

    //Total volume in litre
    @Test
    public void inToLong()
    {
        System.out.println(getValue(25, 5, 2));
    }

    private long getValue(int a, int b, int c)
    {
        long result = (a * b * c) * 1000;

        return result;

    }

    //Display hr and seconds
    @Test
    public void hourAndSecondsValidation()
    {
        System.out.println(convertToSeconds(2));
        System.out.println(convertToSeconds(30));
    }

    private long convertToSeconds(int hour)
    {

        int seconds = hour * 60* 60;
        return seconds;
    }

    @Test
    public void validateListToArrayUsingStreams()
    {

        System.out.println("1 2 3 4 5 6 7 8 9 10");
        System.out.println("2 4 6 8 10 12 14 16 18 20");
        System.out.println("3 6 9 12 15 18 21 24 27 30");
        System.out.println("4 8 12 16 20 24 28 32 36 40");
        System.out.println("5 10 15 20 25 30 35 40 45 50");
        System.out.println("6 12 18 24 30 36 42 48 54 60");
        System.out.println("7 14 21 28 35 42 49 56 63 70");
        System.out.println("8 16 24 32 40 48 56 64 72 80");
        System.out.println("9 18 27 36 45 54 63 72 81 90");
        System.out.println("10 20 30 40 50 60 70 80 90 100");

    }

    @Test
    public void escapeCharacters()
    {

        System.out.println("This is a window path: " + "\"C:\\Program Files\\Java\\jdk1.8.0_172\\bin\"");
        System.out.println("This is a Java string: " + "\\\"C:\\\\Program Files\\\\Java\\\\jdk1.8.0_172\\\\bin\\\"");



    }

    @Test
    public void inputStreamTest() throws IOException {
        InputStream inputStream = System.in;

        Reader reader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(reader);

        String name = bufferedReader.readLine();
        String age = bufferedReader.readLine();

        int userAge = Integer.parseInt(age);




    }


}





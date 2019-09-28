package com.object;

import org.junit.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PuzzleTestDrive
{
    Puzzle[] puzzle = new Puzzle[6];
    private int y = 1;
    private int x;
    private int result;


    @Test
    public void validatePuzzleSolution()
    {
        while (x < 6)
        {
            puzzle[x] = new Puzzle();
            puzzle[x].ivar = y;
            y = y * 10;
            x = x + 1;

        }
        x = 6;

        while (x > 0){
            x = x - 1;
            result = result + puzzle[x].doStuff(x);
        }
        System.out.println("result " + result);
    }

    @Test
    public void validatePuzzleSolution00()
    {
        wordBlanks("cat", "little", "hit", "slowly");

    }

    private void wordBlanks(String cat, String little, String hit, String slowly)
    {
        System.out.println("My "+ little + " " + cat + " " + hit + " " + "very "+ slowly);
    }

    @Test
    public void charByte()
    {
        char x = 39970;
        System.out.println(x);
    }

    @Test
    public void inputStreamTest() throws IOException {
        InputStreamReader reader = new InputStreamReader(System.in);
        while (true){
            int x = reader.read();
            System.out.println(x);
        }

    }

    @Test
    // Better to use BufferedReader class to read data from console/file cos of better performance
    public void bufferedReaderTest() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String s = reader.readLine();
        System.out.println("\"We read this line from the keyboard:");
        System.out.println(s);


    }

    @Test
    public void quatationMark()  {

        System.out.println("My favourite book is \"Twilight\" by Stephen meyer");
        System.out.println("My work file are in \\D:work project\\java");
        System.out.println("She walks in beauty, like the night, \nOf cloudless climes" +
                " and starry skies\nAnd all that's best of dark and bright\nMeet in her aspect and her eyes...");
        System.out.println("\"Escape sequence character\", \u00A9 2019 Bekonhub code");

        System.out.println("\u041c\u0430\u0301\u043e " +

                "\u0426\u0437\u044d\u0434\u0443\u0301\u043d " +

                "\u0028\u043a\u0438\u0442\u002e \u0442\u0440\u0430\u0434\u002e " +

                "\u6bdb\u6fa4\u6771\u002c \u0443\u043f\u0440\u002e " +

                "\u6bdb\u6cfd\u4e1c\u002c \u043f\u0438\u043d\u044c\u0438\u043d\u044c\u003a " +

                "\u004d\u00e1\u006f \u005a\u00e9\u0064\u014d\u006e\u0067\u0029 " +

                "\u2014 \u043a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0439 " +

                "\u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 " +

                "\u0438 \u043f\u043e\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 " +

                "\u0434\u0435\u044f\u0442\u0435\u043b\u044c \u0058\u0058 \u0432\u0435\u043a\u0430\u002c " +

                "\u0433\u043b\u0430\u0432\u043d\u044b\u0439 \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u043a " +

                "\u043c\u0430\u043e\u0438\u0437\u043c\u0430\u002e");

        System.out.println("I want a big salary, and that's why I'm studying Java");
    }

    @Test
    public void logicalTest() throws IOException {

        System.out.println(maximumNumber(25, 5, 10));
        System.out.println(maximumNumber(-10, 5, -15));
        System.out.println(maximumNumber(10, 5, 30));
        System.out.println(maximumNumber(4, 2, 2));

    }

    private int maximumNumber(int num1, int num2, int num3)
    {
        int maxNumber = 0;
        if (num1 > num2 && num1 > num3){
              maxNumber = num1;
              return maxNumber;
        }
        else if(num2 > num1 && num2 > num3){
            maxNumber = num2;
            return maxNumber;
        }
        else if(num3 > num1 && num3 > num2){
             maxNumber = num3;
             return maxNumber;
        }
        else {
            Integer.parseInt("It's a tie");

        }
        return maxNumber;
    }

    @Test
    public void dayOfTheWeekValidation(){
        weekDayIs("-1");
    }

    private void weekDayIs(String weekDay)
    {

        if (Integer.parseInt(weekDay) == 1 )
        {
            System.out.println("Monday");
        }
        else if (Integer.parseInt(weekDay) == 2)
        {
            System.out.println("Tuesday");
        }
        else if(Integer.parseInt(weekDay) == 3)
        {
            System.out.println("Wednesday");
        }
        else if(Integer.parseInt(weekDay) == 4)
        {
            System.out.println("Thursday");
        }
        else if(Integer.parseInt(weekDay) == 5)
        {
            System.out.println("Friday");
        }
        else if(Integer.parseInt(weekDay) == 6)
        {
            System.out.println("Saturday");
        }
        else if(Integer.parseInt(weekDay) == 7)
        {
            System.out.println("Sunday");
        }
        else {
            System.out.println("No such day of the week");
        }
    }

    @Test
    public void descending()
    {
        growLittleMore(17);
    }

    private void growLittleMore(int age)
    {
      boolean m = (age > 0);

      if (m){
          System.out.println(age);
      }


    }

    @Test
    public void numberDescription()
    {

    }



}

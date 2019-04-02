package com.object.test;

import com.object.Dog;
import org.junit.Assert;
import org.junit.Test;


public class DogTest
{
    Dog[] dog = new Dog[13];

    @Test
    public void validateArrayObject(){


        dog[0] = new Dog();
        dog[1] = new Dog();
        dog[2] = new Dog();
        dog[3] = new Dog();
        dog[4] = new Dog();
        dog[5] = new Dog();
        dog[6] = new Dog();
        dog[7] = new Dog();
        dog[8] = new Dog();
        dog[9] = new Dog();
        dog[10] = new Dog();
        dog[11] = new Dog();
        dog[12] = new Dog();


        System.out.println("Total number of elements in dog object is " + dog.length);

        Assert.assertEquals("SMITH", dog[0].name = "smith".toUpperCase());
        System.out.println("Element in Dog object Zero is : " + dog[0].name.toUpperCase());

        Assert.assertEquals("DEMO", dog[1].name = "Demo".toUpperCase());
        System.out.println("Element in Dog object one is : " + dog[1].name.toUpperCase());

        Assert.assertEquals("MANCHESTER", dog[2].name = "Manchester".toUpperCase());
       System.out.println("Element in Dog object two is : " + dog[2].name.toUpperCase());

        Assert.assertEquals("SEGUN", dog[3].name = "Segun".toUpperCase());
        System.out.println("Element in Dog object is four : " + dog[3].name.toUpperCase());

        Assert.assertEquals("ELARO", dog[4].name = "elaro".toUpperCase());
        System.out.println("Element in Dog object five : " + dog[4].name.toUpperCase());

        Assert.assertEquals("MELINDA", dog[5].name = "Melinda".toUpperCase());
        System.out.println("Element in Dog object six : " + dog[5].name.toUpperCase());

        Assert.assertEquals("CLARK", dog[6].name = "Clark".toUpperCase());
        System.out.println("Element in Dog object seven is : " + dog[6].name.toUpperCase());

        Assert.assertEquals("RAYMOND", dog[7].name = "Raymond".toUpperCase());
        System.out.println("Element in Dog Zero eight is : " + dog[7].name.toUpperCase());

        Assert.assertEquals("JOHNSON", dog[8].name = "Johnson".toUpperCase());
        System.out.println("Element in Dog object nine is : " + dog[8].name.toUpperCase());

        Assert.assertEquals("MARK", dog[9].name = "Mark".toUpperCase());
        System.out.println("Element in Dog object ten is : " + dog[9].name.toUpperCase());

        Assert.assertEquals("FORD", dog[10].name = "ford".toUpperCase());
        System.out.println("Element in Dog object eleven : " + dog[10].name.toUpperCase());

        Assert.assertEquals("VINCENT", dog[11].name = "Vincent".toUpperCase());
        System.out.println("Element in Dog object twelve is : " + dog[11].name.toUpperCase());

        Assert.assertEquals("MIDDLETON", dog[12].name = "middleton".toUpperCase());
        System.out.println("Element in Dog object thirteen is : " + dog[12].name.toUpperCase());


        int x  = 0;

        while (x < dog.length){
            dog[x].bark();
             x = x +1;
        }

        Assert.assertEquals(true,dog[12].name.equals("middleton".toUpperCase()));

    }
}

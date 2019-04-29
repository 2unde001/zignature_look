package com.object.test;

import com.object.Books;
import org.junit.Assert;
import org.junit.Test;

public class BookTestDrive
{
    @Test
    public void validateBookTitleAndAuthor()
    {
        Books[] books = new Books[3];

        int x = 0;
        books[0] = new Books();
        books[1] = new Books();
        books[2] = new Books();
        books[0] = new Books();
        books[1] = new Books();
        books[2] = new Books();

        Assert.assertEquals("Java concurrency in practice", books[0].title = "Java concurrency in practice");
        books[1].title = "The clean code";
        books[2].title = "Effective Java";
        books[0].author = "Dr. Heinz Kabutz";
        books[1].author = "Robert C. Martin";
        books[2].author = "Joshua Bloch";

        while (x < 3)
        {
            System.out.println(books[x].title);
            System.out.println(" By ");
            System.out.println(books[x].author);

            x = x + 1;
        }


    }


}

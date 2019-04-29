import java.text.SimpleDateFormat;
import java.util.Date;

import static java.lang.System.*;

public class DateDemo
{
    public  static void main(String[] args)
    {
        Date date = new Date();

        SimpleDateFormat sdf = new SimpleDateFormat("M/d/YYYY");
        SimpleDateFormat sd = new SimpleDateFormat("M/d/yyyy hh:mm:ss");
        out.println(sdf.format(date));
        out.println(sd.format(date));
        out.println(date.toString());
    }
}

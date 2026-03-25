package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The task is intended to occur on the specified date.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OnDateCondition  {

  private ZonedDateTime date;
  private String remarks;

}
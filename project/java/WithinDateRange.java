package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  The task is intended to occur within the specified date range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WithinDateRange  {

  private ZonedDateTime start;
  private ZonedDateTime end;
  private String remarks;

}
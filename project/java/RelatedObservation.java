package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Relates the identified element to a set of referenced observations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedObservation  {

  private String observation-uuid;
  private String remarks;

}
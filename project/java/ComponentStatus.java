package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Describes the operational status of the system component.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentStatus  {

  private String state;
  private String remarks;

}
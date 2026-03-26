package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LocalObjective  {

  private String control-id;
  private String description;
  private List<ControlPart> parts;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}
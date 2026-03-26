package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies the controls being assessed and their control objectives.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReviewedControls  {

  private String description;
  private List<ControlSelection> control-selections;
  private List<ControlObjectiveSelection> control-objective-selections;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}
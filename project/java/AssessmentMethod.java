package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A local definition of a control objective.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentMethod  {

  private String uuid;
  private String description;
  private AssessmentPart part;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}
package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FindingTarget  {

  private String type;
  private String target-id;
  private String title;
  private String description;
  private ImplementationStatus implementation-status;
  private ObjectiveStatus status;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}
package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Identifies the controls being assessed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlSelection  {

  private String description;
  private IncludeAll include-all;
  private List<AssessmentSelectControlById> include-controls;
  private List<AssessmentSelectControlById> exclude-controls;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}